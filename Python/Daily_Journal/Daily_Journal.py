import streamlit as st
import sqlite3
from datetime import datetime

# Database setup
def init_db():
    conn = sqlite3.connect("journal.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS journal_entries (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT,
                    content TEXT
                )''')
    conn.commit()
    conn.close()

def save_entry(content):
    conn = sqlite3.connect("journal.db")
    c = conn.cursor()
    c.execute("INSERT INTO journal_entries (timestamp, content) VALUES (?, ?)", 
              (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), content))
    conn.commit()
    conn.close()

def search_entries(keyword=None, date=None):
    conn = sqlite3.connect("journal.db")
    c = conn.cursor()
    query = "SELECT timestamp, content FROM journal_entries WHERE 1=1"
    params = []
    if keyword:
        query += " AND content LIKE ?"
        params.append(f"%{keyword}%")
    if date:
        query += " AND DATE(timestamp) = ?"
        params.append(date)
    c.execute(query, params)
    results = c.fetchall()
    conn.close()
    return results

# Initialize database
init_db()

# Streamlit app
st.title("Daily Journal/Diary")
st.write("Write and save your daily thoughts, feelings, or activities.")

# Tabs for different functionalities
tab1, tab2 = st.tabs(["Write Entry", "Search Entries"])

# Tab 1: Write Entry
with tab1:
    st.header("Write a New Entry")
    entry_content = st.text_area("What's on your mind today?")
    if st.button("Save Entry"):
        if entry_content.strip():
            save_entry(entry_content)
            st.success("Your entry has been saved!")
        else:
            st.error("Entry cannot be empty.")

# Tab 2: Search Entries
with tab2:
    st.header("Search Past Entries")
    search_date = st.date_input("Search by Date (optional)")
    search_keyword = st.text_input("Search by Keyword (optional)")
    if st.button("Search"):
        results = search_entries(
            keyword=search_keyword if search_keyword.strip() else None,
            date=search_date.strftime("%Y-%m-%d") if search_date else None
        )
        if results:
            st.write("### Search Results:")
            for timestamp, content in results:
                st.write(f"**{timestamp}**")
                st.write(content)
                st.write("---")
        else:
            st.write("No entries found.")