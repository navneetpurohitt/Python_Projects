import streamlit as st
from datetime import datetime
import time
import threading
import winsound

# Function to play alarm sound
def play_alarm():
    for _ in range(5):  # Play sound 5 times
        winsound.Beep(2500, 1000)  # Frequency: 2500 Hz, Duration: 1000 ms
        time.sleep(1)

# Function to check and trigger alarm
def alarm_checker(alarm_time):
    while True:
        current_time = datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            st.warning("Alarm is ringing!")
            play_alarm()
            break
        time.sleep(1)

# Streamlit UI
st.title("Alarm Clock")
st.write("Set an alarm and let it notify you when the time comes!")

# Input for alarm time
alarm_time = st.text_input("Enter alarm time (HH:MM:SS):", placeholder="e.g., 14:30:00")

if st.button("Set Alarm"):
    try:
        # Validate time format
        datetime.strptime(alarm_time, "%H:%M:%S")
        st.success(f"Alarm set for {alarm_time}")
        # Start alarm checker in a separate thread
        threading.Thread(target=alarm_checker, args=(alarm_time,), daemon=True).start()
    except ValueError:
        st.error("Invalid time format! Please use HH:MM:SS.")