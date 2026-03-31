import streamlit as st
from PIL import Image
import io

def compress_image(image, quality):
    img = Image.open(image)
    img_format = img.format
    compressed_image = io.BytesIO()
    img.save(compressed_image, format=img_format, quality=quality)
    compressed_image.seek(0)
    return compressed_image

st.title("Image Quality Compressor")
st.write("Upload an image to compress its quality.")

uploaded_file = st.file_uploader("Drag and drop or click to upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_container_width    =True)
    quality = st.slider("Select Compression Quality (1-100)", min_value=1, max_value=100, value=50)
    
    if st.button("Compress Image"):
        compressed_image = compress_image(uploaded_file, quality)
        st.image(compressed_image, caption="Compressed Image", use_container_width=True)
        st.download_button(
            label="Download Compressed Image",
            data=compressed_image,
            file_name=f"compressed_image.{uploaded_file.name.split('.')[-1]}",
            mime=f"image/{uploaded_file.name.split('.')[-1]}"
        )