import streamlit as st
from PIL import Image
from fpdf import FPDF

# Streamlit app title
st.title("Image to PDF Converter")

# File uploader for image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Convert to PDF button
    if st.button("Convert to PDF"):
        # Save the image as a PDF
        pdf = FPDF()
        pdf.add_page()
        
        # Save the uploaded file temporarily
        temp_image_path = "temp_image.png"
        image.save(temp_image_path)
        
        # Add the image to the PDF
        pdf.image(temp_image_path, x=10, y=10, w=190)  # Adjust dimensions as needed
        
        # Save the PDF
        pdf_output_path = "converted.pdf"
        pdf.output(pdf_output_path)

        # Provide download link
        with open(pdf_output_path, "rb") as pdf_file:
            st.download_button(
                label="Download PDF",
                data=pdf_file,
                file_name="converted.pdf",
                mime="application/pdf"
            )