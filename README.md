# WatchCat - LAN Network Monitoring Tool

## Features
- Monitors all LAN devices' DNS queries
- Logs visited websites with timestamps
- Provides a Flask-based web dashboard for viewing logs

## Installation
```sh
pip install -r requirements.txt
```

## Usage

### 1️⃣ Start Packet Sniffer
```sh
sudo python sniffer.py
```

### 2️⃣ Start Web Dashboard
```sh
python app.py
```
Open [http://localhost:5000](http://localhost:5000) to view logs.

### Export Logs
Click the "Export Logs" button to download logs in CSV format.
