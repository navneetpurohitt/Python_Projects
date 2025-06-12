import streamlit as st
from decimal import Decimal

# Title of the app
st.title("Expense Splitter")

# Input total expenses
total_expenses = st.number_input("Enter the total expenses:", min_value=0.0, format="%.2f")

# Input number of participants
num_participants = st.number_input("Enter the number of participants:", min_value=1, step=1)

if num_participants > 0:
    # Input contribution percentages for each participant
    st.write("Enter the contribution percentage for each participant:")
    contributions = []
    for i in range(num_participants):
        percentage = st.number_input(f"Participant {i + 1} contribution (%):", min_value=0.0, max_value=100.0, format="%.2f")
        contributions.append(percentage)

    # Check if total percentage is valid
    if sum(contributions) != 100.0:
        st.error("The total contribution percentage must equal 100%.")
    else:
        # Calculate the amount each participant needs to pay
        st.write("### Payment Details:")
        for i, percentage in enumerate(contributions):
            amount = Decimal(total_expenses) * Decimal(percentage) / Decimal(100)
            st.write(f"Participant {i + 1} needs to pay: ${amount:.2f}")