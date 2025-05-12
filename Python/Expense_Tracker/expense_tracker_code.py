import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from streamlit_card import card

# Set page configuration
st.set_page_config(page_title="Expense Tracker", page_icon="💰", layout="wide")
st.title("Expense Tracker")
st.write("Track your expenses and visualize your spending patterns.")

# Sidebar options
option = st.sidebar.radio("Choose an action", ["Add item", "Delete item", "Show items"])

# Load the CSV file
file_path = "expense_data.csv"
try:
    data = pd.read_csv(file_path)
except FileNotFoundError:
    data = pd.DataFrame(columns=["Date", "Category", "Description", "Amount"])

if option == "Add item":
    st.subheader("Add a new expense")
    with st.form("add_item_form"):
        # Date,Account,Category,Subcategory,Note,INR,Income/Expense,Note,Amount,Currency,Account

        date = st.date_input("Date", pd.to_datetime("today"))
        account = st.selectbox("Account", ["Cash", "Credit Card", "Bank Transfer"])
        category = st.selectbox("Category", ["Food", "Transport", "Entertainment", "Utilities", "Other"])
        subcategory = st.text_input("Subcategory")
        note = st.text_input("Note")
        amount = st.number_input("Amount", min_value=0.0, format="%.2f")
        currency = st.selectbox("Currency", ["INR", "USD", "EUR"])
        income_expense = st.selectbox("Income/Expense", ["Income", "Expense"])
        

        submitted = st.form_submit_button("Add Expense")
        if submitted:
            new_expense = {
                "Date": date,
                "Account": account,
                "Category": category,
                "Subcategory": subcategory,
                "Note": note,
                "Amount": amount,
                "Currency": currency,
                "Income/Expense": income_expense
            }
            data = pd.concat([data, pd.DataFrame([new_expense])], ignore_index=True)
            data.to_csv(file_path, index=False)
            st.success("Expense added successfully!")

elif option == "Delete item":
    st.subheader("Delete an expense")
    if data.empty:
        st.write("No expenses to delete.")
    else:
        for index, row in data.iterrows():
            st.write(f"**{index}**: {row['Date']} - {row['Category']} - {row['Amount']}")
            if st.button(f"Delete {index}", key=index):
                data = data.drop(index)
                data.to_csv(file_path, index=False)
                st.success("Expense deleted successfully!")
               

elif option == "Show items":
    
 
    categories = data["Category"].unique()
   
    selected_category = st.selectbox("Select a category", categories)
 

    filtered_data = data[data["Category"] == selected_category]
    col1, col2 = st.columns(2)
    with col1:
        st.header("Show all expenses")
        sum = data[data["Category"] == selected_category]["Amount"].sum()
        card(
            title="Total Amount",
            text=f"Total amount spent in {selected_category}: {sum}"
        )
    st.dataframe(filtered_data)