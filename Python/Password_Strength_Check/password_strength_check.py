import re
import streamlit as st

def check_password_strength(password):
    # Define the regex for password validation
    length_error = len(password) < 8
    digit_error = not re.search(r"\d", password)
    uppercase_error = not re.search(r"[A-Z]", password)
    lowercase_error = not re.search(r"[a-z]", password)
    symbol_error = not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    # Check for errors
    if length_error:
        return "Password must be at least 8 characters long."
    if digit_error:
        return "Password must contain at least one digit."
    if uppercase_error:
        return "Password must contain at least one uppercase letter."
    if lowercase_error:
        return "Password must contain at least one lowercase letter."
    if symbol_error:
        return "Password must contain at least one special character (!@#$%^&*(),.?\":{}|<>)."

    return "Strong password!"

# Streamlit app
st.title("Password Strength Checker")

password = st.text_input("Enter your password:", type="password")

if password:
    result = check_password_strength(password)
    if result == "Strong password!":
        st.success(result)
    else:
        st.error(result)