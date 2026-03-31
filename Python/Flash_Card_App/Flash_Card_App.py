import streamlit as st
import sqlite3
import random

# Database setup
def init_db():
    conn = sqlite3.connect("flashcards.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS flashcards (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    question TEXT NOT NULL,
                    answer TEXT NOT NULL,
                    correct_count INTEGER DEFAULT 0,
                    incorrect_count INTEGER DEFAULT 0
                )''')
    conn.commit()
    conn.close()

def add_flashcard(question, answer):
    conn = sqlite3.connect("flashcards.db")
    c = conn.cursor()
    c.execute("INSERT INTO flashcards (question, answer) VALUES (?, ?)", (question, answer))
    conn.commit()
    conn.close()

def get_random_flashcard():
    conn = sqlite3.connect("flashcards.db")
    c = conn.cursor()
    c.execute("SELECT * FROM flashcards ORDER BY RANDOM() LIMIT 1")
    flashcard = c.fetchone()
    conn.close()
    return flashcard

def update_flashcard_status(card_id, correct):
    conn = sqlite3.connect("flashcards.db")
    c = conn.cursor()
    if correct:
        c.execute("UPDATE flashcards SET correct_count = correct_count + 1 WHERE id = ?", (card_id,))
    else:
        c.execute("UPDATE flashcards SET incorrect_count = incorrect_count + 1 WHERE id = ?", (card_id,))
    conn.commit()
    conn.close()

def get_progress():
    conn = sqlite3.connect("flashcards.db")
    c = conn.cursor()
    c.execute("SELECT SUM(correct_count), SUM(incorrect_count) FROM flashcards")
    correct, incorrect = c.fetchone()
    conn.close()
    return correct or 0, incorrect or 0

# Streamlit UI
st.title("Flashcard App")

# Initialize database
init_db()

# Add new flashcards
st.header("Add New Flashcard")
with st.form("add_flashcard_form"):
    question = st.text_input("Question")
    answer = st.text_input("Answer")
    submitted = st.form_submit_button("Add Flashcard")
    if submitted and question and answer:
        add_flashcard(question, answer)
        st.success("Flashcard added!")

# Practice flashcards
st.header("Practice Flashcards")
flashcard = get_random_flashcard()
if flashcard:
    st.write(f"**Question:** {flashcard[1]}")
    show_answer = st.button("Show Answer")
    if show_answer:
        st.write(f"**Answer:** {flashcard[2]}")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Correct"):
                update_flashcard_status(flashcard[0], True)
                st.experimental_rerun()
        with col2:
            if st.button("Incorrect"):
                update_flashcard_status(flashcard[0], False)
                st.experimental_rerun()
else:
    st.write("No flashcards available. Add some to get started!")

# Progress tracking
st.header("Progress")
correct, incorrect = get_progress()
st.write(f"Correct Answers: {correct}")
st.write(f"Incorrect Answers: {incorrect}")
if correct + incorrect > 0:
    st.progress(correct / (correct + incorrect))