import streamlit as st
import random 
import string

st.title("Password Generator")
st.write("Generate a random password with the specified length and character types.")

length = st.sidebar.number_input("Length of Password", min_value=1, max_value=100, value=12, step=1)

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
        # Generate a random password
    password = ''.join(random.choice(characters) for i in range(length))
    return password


password = generate_password(length)
st.code("Generated Password: " + password)

button_reshuffule = st.sidebar.button("Reshuffle Password")
if button_reshuffule:
    password = generate_password(length)