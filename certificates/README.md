# 📋 Daily Task Tracker

A beautiful web-based daily task tracker with progress visualization.

## Features
- ✅ Daily checklists with date — add/complete/delete tasks
- 🎯 Priority levels: High 🔥 / Mid ⚡ / Low 🌿
- 📊 Progress ring & bar per day
- 📈 Analytics view: line chart, bar chart, heatmap
- 🗂 Consolidated all-days view with progress bars
- 💾 Data saved as JSON files in `data/` folder (one file per day)

## Setup

```bash
pip install -r requirements.txt
python app.py
```

Then open → **http://localhost:5050**

## Data Storage
All tasks are stored in the `data/` folder as `YYYY-MM-DD.json` files.
Example: `data/2025-03-31.json`
