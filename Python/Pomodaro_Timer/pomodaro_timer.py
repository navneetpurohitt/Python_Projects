import streamlit as st
import time

# Title
st.title("Pomodoro Timer")

# Input for work hours and break timings
work_hours = st.number_input("Enter work duration (in minutes):", min_value=1, value=25)
break_minutes = st.number_input("Enter break duration (in minutes):", min_value=1, value=5)
current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
st.write(f"Current Time: {current_time}")
time.sleep(1)

# Start button
if st.button("Start Timer"):
    # Work Timer
    st.write("Work Timer Started!")
    timer_placeholder = st.empty()
    for i in range(work_hours * 60, 0, -1):
        mins, secs = divmod(i, 60)
        timer = f"{mins:02d}:{secs:02d}"
        timer_placeholder.markdown(
        f"<h1 style='color: red; font-size: 80px;'>{timer}</h1>", 
        unsafe_allow_html=True
    )
        # timer_placeholder.metric(f"Pomodaro Timer", value=f"{mins:02d}:{secs:02d}")
        time.sleep(1)
   

    # Break Timer
    timer_placeholder = st.empty()
    for i in range(break_minutes * 60, 0, -1):
        mins, secs = divmod(i, 60)
        timer = f"{mins:02d}:{secs:02d}"
        timer_placeholder.markdown(
        f"<h1 style='color: red; font-size: 80px;'>{timer}</h1>", 
        unsafe_allow_html=True
    )
       


    st.write("Pomodoro Session Complete!")