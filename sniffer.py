from scapy.all import sniff, DNSQR
import sqlite3
from datetime import datetime

# Database setup
conn = sqlite3.connect("monitor_logs.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ip TEXT,
    domain TEXT,
    timestamp TEXT
)
""")
conn.commit()

def packet_handler(packet):
    if packet.haslayer(DNSQR) and packet.haslayer("IP"):
        src_ip = packet["IP"].src  # Source IP of request
        domain = packet[DNSQR].qname.decode()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        cursor.execute("INSERT INTO logs (ip, domain, timestamp) VALUES (?, ?, ?)", (src_ip, domain, timestamp))
        conn.commit()
        print(f"[{timestamp}] {src_ip} visited {domain}")

# Capture all DNS traffic on LAN
print("Monitoring all devices on LAN...")
sniff(filter="udp port 53", prn=packet_handler, store=False)
