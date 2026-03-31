import streamlit as st

def loan_application():
    st.title("Loan Application")
    st.write("Fill out the form below to apply for a loan.")
    
    name = st.text_input("Name")
    amount = st.number_input("Loan Amount", min_value=1000, max_value=100000, step=1000)
    duration = st.number_input("Loan Duration (in months)", min_value=1, max_value=60, step=1)
    income = st.number_input("Monthly Income", min_value=0, step=100)

    if st.button("Submit Application"):
        if name and amount and duration and income:
            st.success("Loan application submitted successfully!")
        else:
            st.error("Please fill out all fields.")

def check_loan_status():
    st.title("Check Loan Status")
    loan_id = st.text_input("Enter your Loan ID")

    if st.button("Check Status"):
        if loan_id:
            st.success(f"Status for Loan ID {loan_id}: Approved")
        else:
            st.error("Please enter a Loan ID.")

def calculate_eligibility():
    st.title("Loan Eligibility Calculator")
    income = st.number_input("Monthly Income", min_value=0, step=100)
    existing_loans = st.number_input("Existing Loan Amount", min_value=0, step=100)

    if st.button("Calculate Eligibility"):
        eligibility = income * 0.5 - existing_loans
        if eligibility > 0:
            st.success(f"You are eligible for a loan up to: ${eligibility:.2f}")
        else:
            st.error("You are not eligible for a loan.")

def main():
    st.sidebar.title("Loan Services")
    option = st.sidebar.selectbox("Select an option", ["Apply for a Loan", "Check Loan Status", "Calculate Eligibility"])

    if option == "Apply for a Loan":
        loan_application()
    elif option == "Check Loan Status":
        check_loan_status()
    elif option == "Calculate Eligibility":
        calculate_eligibility()

if __name__ == "__main__":
    main()