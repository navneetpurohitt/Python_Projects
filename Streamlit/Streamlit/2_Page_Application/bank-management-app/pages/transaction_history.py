import streamlit as st
import pandas as pd

# Sample data for demonstration purposes
data = {
    'Transaction ID': [1, 2, 3, 4],
    'Account Number': ['123456', '123456', '654321', '654321'],
    'Date': ['2023-01-01', '2023-01-15', '2023-02-01', '2023-02-10'],
    'Amount': [100.0, -50.0, 200.0, -100.0],
    'Description': ['Deposit', 'Withdrawal', 'Deposit', 'Withdrawal']
}

# Create a DataFrame
transactions_df = pd.DataFrame(data)

st.title('Transaction History')

# Input for account number
account_number = st.text_input('Enter Account Number')

# Filter transactions based on account number
if account_number:
    filtered_transactions = transactions_df[transactions_df['Account Number'] == account_number]
    if not filtered_transactions.empty:
        st.write(filtered_transactions)
    else:
        st.write('No transactions found for this account number.')
else:
    st.write('Please enter an account number to view transaction history.')