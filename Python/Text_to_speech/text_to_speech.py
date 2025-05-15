from gtts import gTTS
import streamlit as st

def text_to_speech(text, filename):
    try:
        tts = gTTS(text=text, lang='en')
        tts.save(filename)
        print(f"Audio file saved as {filename}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    st.title("Text to Speech Converter")
    
    # Input text from the user
    text = st.text_area("Enter the text to convert to speech:", "")
    
    # Input filename from the user
    filename = st.text_input("Enter the output filename (with .mp3 extension):", "output.mp3")
    
    if st.button("Convert to Speech"):
        if text.strip() and filename.strip():
            text_to_speech(text, filename)
            st.success(f"Audio file saved as {filename}")
            # Display a download link for the file
            with open(filename, "rb") as audio_file:
                st.download_button(
                    label="Download Audio File",
                    data=audio_file,
                    file_name=filename,
                    mime="audio/mpeg"
                )
            st.audio(filename, format="audio/mp3")
        else:
            st.error("Please provide both text and a valid filename.")