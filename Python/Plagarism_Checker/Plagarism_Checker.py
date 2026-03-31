import os
from difflib import SequenceMatcher
import streamlit as st

def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        st.error(f"File not found: {file_path}")
        return None

def calculate_similarity(text1, text2):
    return SequenceMatcher(None, text1, text2).ratio()

def check_plagiarism(file1, file2):
    text1 = read_file(file1)
    text2 = read_file(file2)

    if text1 is None or text2 is None:
        return None

    return calculate_similarity(text1, text2)

# Streamlit UI
st.title("Plagiarism Checker")

uploaded_file1 = st.file_uploader("Upload the first file", type=["txt"])
uploaded_file2 = st.file_uploader("Upload the second file", type=["txt"])

if st.button("Check Plagiarism"):
    if uploaded_file1 is not None and uploaded_file2 is not None:
        # Read the uploaded files
        text1 = uploaded_file1.read().decode("utf-8")
        text2 = uploaded_file2.read().decode("utf-8")

        # Calculate similarity
        similarity = calculate_similarity(text1, text2)
        st.success(f"Similarity: {similarity * 100:.2f}%")
    else:
        st.error("Please upload both files to check plagiarism.")