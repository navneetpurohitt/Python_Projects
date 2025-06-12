import streamlit as st
import random
from datetime import date

# List of quotes
quotes = [
    "The best way to predict the future is to create it. - Peter Drucker",
    "Your time is limited, so don’t waste it living someone else’s life. - Steve Jobs",
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Success is not the key to happiness. Happiness is the key to success. - Albert Schweitzer",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "Act as if what you do makes a difference. It does. - William James",
    "Keep your face always toward the sunshine—and shadows will fall behind you. - Walt Whitman",
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
    "Do what you can, with what you have, where you are. - Theodore Roosevelt",
    "In the middle of every difficulty lies opportunity. - Albert Einstein"
]

# Function to get a random quote based on the current date
def get_daily_quote():
    today = date.today()
    random.seed(today.toordinal())  # Seed based on the current date
    return random.choice(quotes)

# Streamlit app
st.title("Daily Inspirational Quote")
st.write("Start your day with a dose of inspiration!")

quote = get_daily_quote()
st.markdown(f"### 🌟 {quote}")