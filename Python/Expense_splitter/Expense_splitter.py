import streamlit as st
from decimal import Decimal, ROUND_HALF_UP

# Function to calculate expenses
def calculate_expenses(total_expense, participants):
    per_person = (total_expense / len(participants)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    balances = {name: per_person - amount for name, amount in participants.items()}
    return balances

# Streamlit App
st.title("Expense Splitter")

# Input total expense
st.header("Enter Total Expense")
total_expense = st.number_input("Total Expense", min_value=0.0, format="%.2f")
total_expense = Decimal(str(total_expense))

# Input participants and their contributions
st.header("Participants and Contributions")
participants = {}
num_participants = st.number_input("Number of Participants", min_value=1, step=1)

for i in range(num_participants):
    name = st.text_input(f"Participant {i + 1} Name", key=f"name_{i}")
    contribution = st.number_input(f"{name}'s Contribution", min_value=0.0, format="%.2f", key=f"contribution_{i}")
    if name:
        participants[name] = Decimal(str(contribution))

# Calculate and display results
if st.button("Calculate"):
    if participants and total_expense > 0:
        balances = calculate_expenses(total_expense, participants)
        st.header("Results")
        for name, balance in balances.items():
            if balance > 0:
                st.write(f"{name} should receive: ${balance}")
            elif balance < 0:
                st.write(f"{name} owes: ${-balance}")
            else:
                st.write(f"{name} is settled.")
    else:
        st.error("Please enter valid inputs.")