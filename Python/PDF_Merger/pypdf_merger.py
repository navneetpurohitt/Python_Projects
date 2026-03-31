from PyPDF2 import  PdfReader, PdfWriter
import os
import streamlit as st
st.title("PDF Merger")
st.header("Created and Developed by Navneet Purohit")
uploaded_pdfs = st.file_uploader("Upload PDF files", type=["pdf"], accept_multiple_files=True)

output_file = st.text_input("Output file name", "Merged.pdf")

pdf_writer = PdfWriter()

if st.button("Merge PDF") and uploaded_pdfs:
    for pdf_file in uploaded_pdfs:
        reader = PdfReader(pdf_file)
        for page in reader.pages:
            pdf_writer.add_page(page)
      
    if st.success("PDFs merged successfully!"):
        with open(output_file, "rb") as f:
            st.download_button(
                label="Download PDF File",
                data=f,
                file_name=output_file,
                mime="text/plain"
            )
    else:
        st.error("Error merging PDFs. Please try again.")
else:   
    st.warning("Please upload at least one PDF file to merge.")
# This code is a simple PDF merger using PyPDF2 and Streamlit. It allows users to upload multiple PDF files, merge them into one, and download the merged file.


