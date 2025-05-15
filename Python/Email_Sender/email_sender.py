import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, recipient_email, subject, template, template_data):
    """
    Sends an email using the provided sender credentials, recipient email, subject, 
    and a template with dynamic data.

    Args:
        sender_email (str): The sender's email address.
        sender_password (str): The sender's email password.
        recipient_email (str): The recipient's email address.
        subject (str): The subject of the email.
        template (str): The email body template with placeholders.
        template_data (dict): A dictionary containing data to fill the placeholders in the template.
    """
    try:
        # Create the email object
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Format the template with provided data
        email_body = template.format(**template_data)
        msg.attach(MIMEText(email_body, 'plain'))  # Attach the email body as plain text

        # Connect to the SMTP server and send the email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Start TLS encryption
            server.login(sender_email, sender_password)  # Log in to the SMTP server
            server.send_message(msg)  # Send the email

        print("Email sent successfully!")  # Notify the user of success
    except Exception as e:
        # Handle any exceptions that occur during the email sending process
        print(f"Failed to send email: {e}")

# Example usage
if __name__ == "__main__":
    # Sender's email credentials
    st.title("Email Sender")
    st.write("Fill in the details below to send an email.")
    
    sender_email = st.text_input("Sender Email")
    sender_password = st.text_input("Sender Password", type="password")
    print(sender_email, sender_password)

    # Recipient's email address
    recipient_email = st.text_input("Recipient Email")
    

    # Subject of the email
    subject = st.text_input("Email Subject")
    
    # Email template with placeholders
    template = """
    Hi {name},

    This is a test email sent using Python.

    Regards,
    {sender_name}
    """
    # Data to fill the placeholders in the template
    template_data = {
        "name": "John Doe",
        "sender_name": "Your Name"
    }
    if st.button("Send Email"):
        # Validate inputs
        if not sender_email or not sender_password or not recipient_email or not subject:
            st.error("Please fill in all fields.")
        else:
            # Call the function to send the email
            send_email(sender_email, sender_password, recipient_email, subject, template, template_data)
            st.success("Email sent successfully!")
    # Call the function to send the email
        send_email(sender_email, sender_password, recipient_email, subject, template, template_data)