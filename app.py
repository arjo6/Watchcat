from flask import Flask, render_template
import sqlite3
import pandas as pd

app = Flask(__name__)

def get_logs():
    conn = sqlite3.connect("monitor_logs.db")
    df = pd.read_sql_query("SELECT * FROM logs ORDER BY timestamp DESC", conn)
    conn.close()
    return df

@app.route("/")
def index():
    logs = get_logs()
    return render_template("index.html", logs=logs.to_dict(orient="records"))

@app.route("/export")
def export_csv():
    logs = get_logs()
    logs.to_csv("monitor_logs.csv", index=False)
    return "Logs exported as monitor_logs.csv"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
