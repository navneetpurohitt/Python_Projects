import qrcode
import streamlit as st
def generate_qr_code(data, file_name):
    """
    Generate a QR code and save it as an image file.

    :param data: The data to encode in the QR code.
    :param file_name: The name of the file to save the QR code image.
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)
    
    st.image(file_name, caption="Generated QR Code", use_column_width=True)
    print(f"QR code saved as {file_name}")

if __name__ == "__main__":
    # Example usage
    st.title("QR Code Generator")
    data_to_encode = st.text_input("Enter data to encode in QR code:")
    generate = st.button("Generate QR Code")
    
    output_file = "qrcode.png"
    if generate:
        generate_qr_code(data_to_encode, output_file)