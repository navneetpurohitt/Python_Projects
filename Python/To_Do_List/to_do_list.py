import streamlit as st
import pandas as pd
import datetime
import json

st.title("Navneet To-Do List for " + str(datetime.date.today()))

st.subheader("Manage your tasks efficiently")

st.sidebar.write("Chose an option:")
input_from_radio = st.sidebar.radio("Options", ("Add Task", "View Tasks", "Delete Task","Clear All Tasks"))

if input_from_radio == "Add Task":
    st.header("Add a new task")
    task_name = st.text_input("Task Name")
    task_description = st.text_area("Task Description")
    task_due_date = st.date_input("Due Date", datetime.date.today())
    task_priority = st.selectbox("Priority", ["High", "Medium", "Low"])
    task_status = st.selectbox("Status", ["Not Started", "In Progress", "Completed"])

    if st.button("Add Task"):
        if task_name and task_description:
            new_task = {
                "Task Name": task_name,
                "Description": task_description,
                "Due Date": str(task_due_date),
                "Priority": task_priority,
                "Status": task_status
            }
            try:
                with open("tasks.json", "r") as file:
                    tasks = json.load(file)
            except FileNotFoundError:
                tasks = []

            tasks.append(new_task)

            with open("tasks.json", "w") as file:
                json.dump(tasks, file)

            st.success("Task added successfully!")
        else:
            st.error("Please fill in all fields.")
if input_from_radio == ("View Tasks"):
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
        if tasks:
            st.write(pd.DataFrame(tasks))
        else:
            st.write("No tasks found.")
    except FileNotFoundError:
        st.write("No tasks found.")
if input_from_radio == ("Delete Task"):
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
        if tasks:
            task_to_delete = st.selectbox("Select Task to Delete", [task["Task Name"] for task in tasks])
            if st.button("Delete"):
                tasks = [task for task in tasks if task["Task Name"] != task_to_delete]
                with open("tasks.json", "w") as file:
                    json.dump(tasks, file)
                st.success("Task deleted successfully!")
        else:
            st.write("No tasks found.")
    except FileNotFoundError:
        st.write("No tasks found.")

if input_from_radio == ("Clear All Tasks"):
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
        if tasks:
            st.write(pd.DataFrame(tasks))
        else:
            st.write("No tasks found.")
    except FileNotFoundError:
        st.write("No tasks found.")
    if st.button("Clear All Tasks"):
        with open("tasks.json", "w") as file:
            json.dump([], file)
        st.success("All tasks cleared successfully!")