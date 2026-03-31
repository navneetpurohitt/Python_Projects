import streamlit as st

# Set the title of the application
st.title("Bank Management Application")

# Create a sidebar for navigation
st.sidebar.title("Navigation")
pages = {
    "Account Management": "pages/account_management.py",
    "Transaction History": "pages/transaction_history.py",
    "Loan Services": "pages/loan_services.py",
    "Customer Support": "pages/customer_support.py"
}

# Create a selectbox for page selection
selected_page = st.sidebar.selectbox("Select a page", list(pages.keys()))

# Load the selected page
if selected_page:
    try:
        page_module = __import__(pages[selected_page].replace('.py', '').replace('/', '.'), fromlist=[''])
        if hasattr(page_module, 'run'):
            page_module.run()
        else:
            st.error(f"The selected page '{selected_page}' does not have a 'run' function.")
    except ModuleNotFoundError:
        st.error(f"The module for the selected page '{selected_page}' could not be found.")