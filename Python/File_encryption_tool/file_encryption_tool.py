import streamlit as st
from cryptography.fernet import Fernet

# Function to generate and save a key
def generate_key(key_file):
    key = Fernet.generate_key()
    with open(key_file, 'wb') as file:
        file.write(key)
    print(f"Key saved to {key_file}")

# Function to load the key
def load_key(key_file):
    with open(key_file, 'rb') as file:
        return file.read()

# Function to encrypt a file
def encrypt_file(input_file, output_file, key):
    fernet = Fernet(key)
    with open(input_file, 'rb') as file:
        data = file.read()
    encrypted_data = fernet.encrypt(data)
    with open(output_file, 'wb') as file:
        file.write(encrypted_data)
    print(f"File {input_file} encrypted to {output_file}")

# Function to decrypt a file
def decrypt_file(input_file, output_file, key):
    fernet = Fernet(key)
    with open(input_file, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(output_file, 'wb') as file:
        file.write(decrypted_data)
    print(f"File {input_file} decrypted to {output_file}")

# Example usage
if __name__ == "__main__":
    key_file = "encryption.key"
    generate_key(key_file)  # Generate and save a key

    key = load_key(key_file)  # Load the key
    st.title("File Encryption Tool")
    uploaded_file =  st.file_uploader("Upload a file to encrypt")
    if uploaded_file is not None:
        file_data = uploaded_file.read()  # Read the file content
        if st.button("Encrypt File"):
            fernet = Fernet(key)
            encrypted_data = fernet.encrypt(file_data)
            st.download_button("Download Encrypted File", encrypted_data, file_name="encrypted_file")
            st.success("File encrypted successfully!")


    # Decrypt the file
    decrypted_file = st.file_uploader("Upload a file to decrypt")
    if decrypted_file is not None:
        file_data = decrypted_file.read()  # Read the file content
        if st.button("Decrypt File"):
            fernet = Fernet(key)
            try:
                decrypted_data = fernet.decrypt(file_data)
                st.download_button("Download Decrypted File", decrypted_data, file_name="decrypted_file")
                st.success("File decrypted successfully!")  
            except Exception as e:
                st.error("Decryption failed. Please ensure the file was encrypted with the correct key.")