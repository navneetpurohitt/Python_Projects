import streamlit as st
from PyPDF2 import PdfReader

def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def main():
    st.title("PDF Text Extractor")
    st.write("Upload a PDF file to extract its text content.")

    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    if uploaded_file is not None:
        try:
            extracted_text = extract_text_from_pdf(uploaded_file)
            st.subheader("Extracted Text:")
            st.text_area("PDF Content", extracted_text, height=400)
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()