from flask import Flask, render_template, request, jsonify
import json
import os
from datetime import datetime, timedelta
from pathlib import Path

#Create by Navneet Purohit
app = Flask(__name__)
DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

def get_file_path(date_str):
    return DATA_DIR / f"{date_str}.json"

def load_day(date_str):
    fp = get_file_path(date_str)
    if fp.exists():
        with open(fp) as f:
            return json.load(f)
    return {"date": date_str, "tasks": []}

def save_day(date_str, data):
    with open(get_file_path(date_str), "w") as f:
        json.dump(data, f, indent=2)

def all_dates():
    files = sorted(DATA_DIR.glob("*.json"), reverse=True)
    return [f.stem for f in files]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/day/<date_str>", methods=["GET"])
def get_day(date_str):
    return jsonify(load_day(date_str))

@app.route("/api/day/<date_str>", methods=["POST"])
def save_day_api(date_str):
    data = request.json
    data["date"] = date_str
    save_day(date_str, data)
    return jsonify({"status": "ok"})

@app.route("/api/dates")
def get_dates():
    return jsonify(all_dates())

@app.route("/api/consolidated")
def consolidated():
    dates = all_dates()
    result = []
    for d in dates:
        day = load_day(d)
        tasks = day.get("tasks", [])
        total = len(tasks)
        done = sum(1 for t in tasks if t.get("done"))
        result.append({
            "date": d,
            "total": total,
            "done": done,
            "pct": round((done / total * 100) if total else 0, 1)
        })
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, port=5050)
