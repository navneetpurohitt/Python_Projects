import streamlit as st
from pdf2docx import Converter
import os

def pdf_to_word(pdf_file, word_file):
    # Create a Converter object
    cv = Converter(pdf_file)
            
    # Convert PDF to Word
    cv.convert(word_file, start=0, end=None)  # Convert all pages
    cv.close()

# Streamlit app
def main():
    st.title("PDF to Word Converter")
    st.write("Upload a PDF file to convert it to a Word document.")

    # File uploader
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file is not None:
        # Save the uploaded file temporarily
        temp_pdf_path = "temp_uploaded_file.pdf"
        with open(temp_pdf_path, "wb") as f:
            f.write(uploaded_file.read())

        # Output Word file path
        output_word_path = "output.docx"

        # Convert PDF to Word
        if st.button("Convert"):
            pdf_to_word(temp_pdf_path, output_word_path)
            st.success("Conversion complete!")
            with open(output_word_path, "rb") as word_file:
                # Add background image
                import base64

                def get_base64_of_bin_file(bin_file):
                    with open(bin_file, 'rb') as f:
                        data = f.read()
                    return base64.b64encode(data).decode()

                img_path = "D:\\Projects\\Git\\Python_Projects\\Python\\PDF_to_Word\\image.jpg"
                img_base64 = get_base64_of_bin_file(img_path)

                page_bg_img = f'''
                <style>
                body {{
                    background-image: url("data:image/jpg;base64,{img_base64}");
                    background-size: cover;
                }}
                </style>
                '''
                st.markdown(page_bg_img, unsafe_allow_html=True)

                # Existing download button code
                st.download_button(
                    label="Download Word File",
                    data=word_file,
                    file_name="output.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                )

        # Clean up temporary files
        if os.path.exists(temp_pdf_path):
            os.remove(temp_pdf_path)
        if os.path.exists(output_word_path):
            os.remove(output_word_path)

if __name__ == "__main__":
    main()