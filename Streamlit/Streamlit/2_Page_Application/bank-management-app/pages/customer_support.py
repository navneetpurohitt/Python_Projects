import streamlit as st

def display_faq():
    st.header("Frequently Asked Questions")
    faqs = {
        "How can I reset my password?": "You can reset your password by clicking on the 'Forgot Password' link on the login page.",
        "How do I contact customer support?": "You can contact customer support by filling out the contact form below.",
        "What are the bank's operating hours?": "Our operating hours are Monday to Friday, 9 AM to 5 PM.",
        "How can I check my account balance?": "You can check your account balance by logging into your account and navigating to the account overview section."
    }
    
    for question, answer in faqs.items():
        st.subheader(question)
        st.write(answer)

def contact_form():
    st.header("Contact Us")
    with st.form(key='contact_form'):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submit_button = st.form_submit_button(label='Submit')
        
        if submit_button:
            st.success("Thank you for your message! We will get back to you shortly.")

def main():
    st.title("Customer Support")
    display_faq()
    st.write("---")
    contact_form()

if __name__ == "__main__":
    main()