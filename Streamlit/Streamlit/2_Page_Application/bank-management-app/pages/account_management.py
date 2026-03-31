import streamlit as st

# Function to create a new account
def create_account():
    st.subheader("Create Account")
    account_name = st.text_input("Account Name")
    initial_balance = st.number_input("Initial Balance", min_value=0.0)
    
    if st.button("Create Account"):
        # Logic to create account (placeholder)
        st.success(f"Account '{account_name}' created with balance ${initial_balance:.2f}.")

# Function to update an existing account
def update_account():
    st.subheader("Update Account")
    account_id = st.text_input("Account ID")
    new_balance = st.number_input("New Balance", min_value=0.0)
    
    if st.button("Update Account"):
        # Logic to update account (placeholder)
        st.success(f"Account '{account_id}' updated to balance ${new_balance:.2f}.")

# Function to delete an account
def delete_account():
    st.subheader("Delete Account")
    account_id = st.text_input("Account ID")
    
    if st.button("Delete Account"):
        # Logic to delete account (placeholder)
        st.success(f"Account '{account_id}' deleted.")

# Function to display account details
def display_account_details():
    st.subheader("Account Details")
    account_id = st.text_input("Enter Account ID to view details")
    
    if st.button("View Details"):
        # Logic to fetch and display account details (placeholder)
        st.write(f"Details for account '{account_id}':")
        st.write("Account Name: Sample Name")
        st.write("Balance: $1000.00")

# Main function to manage account operations
def main():
    st.title("Account Management")
    menu = ["Create Account", "Update Account", "Delete Account", "View Account Details"]
    choice = st.sidebar.selectbox("Select Operation", menu)

    if choice == "Create Account":
        create_account()
    elif choice == "Update Account":
        update_account()
    elif choice == "Delete Account":
        delete_account()
    elif choice == "View Account Details":
        display_account_details()

if __name__ == "__main__":
    main()