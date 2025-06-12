import time
import tkinter as tk
from tkinter import messagebox

def set_alarm(alarm_time, task):
    while True:
        current_time = time.strftime("%H:%M:%S")
        if current_time == alarm_time:
            show_reminder(task)
            break
        time.sleep(1)

def show_reminder(task):
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    messagebox.showinfo("Alarm", f"Reminder: {task}")
    root.destroy()

if __name__ == "__main__":
    print("Welcome to the Alarm Clock!")
    alarm_time = input("Enter the alarm time in HH:MM:SS format: ")
    task = input("Enter the task to be reminded of: ")
    print(f"Alarm set for {alarm_time} to remind you of: {task}")
    set_alarm(alarm_time, task)