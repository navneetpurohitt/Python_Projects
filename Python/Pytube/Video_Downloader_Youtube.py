import yt_dlp
import streamlit as st

if __name__ == "__main__":
    video_url = st.text_input("Enter the YouTube video URL: ", key="video_url")
    try:
        download_type = st.sidebar.radio("Select Download Type:", ("Video", "Audio"))

        if st.button("Download"):
            st.write("Downloading...")

            # Progress bar
            progress_bar = st.progress(0)
            status_text = st.empty()

            def progress_hook(d):
                if d['status'] == 'downloading':
                    total_bytes = d.get('total_bytes', 0)
                    downloaded_bytes = d.get('downloaded_bytes', 0)
                    if total_bytes > 0:
                        progress = int(downloaded_bytes / total_bytes * 100)
                        progress_bar.progress(progress)
                        status_text.text(f"Downloaded: {downloaded_bytes / (1024 * 1024):.2f} MB / {total_bytes / (1024 * 1024):.2f} MB")
                elif d['status'] == 'finished':
                    progress_bar.progress(100)
                    status_text.text("Download complete!")

            # Update yt-dlp options based on download type
            def download_with_progress(url, path='.', download_type="Video"):
                ydl_opts = {
                    'format': 'bestaudio/best' if download_type == "Audio" else 'best',
                    'outtmpl': f'{path}/%(title)s.%(ext)s',
                    'progress_hooks': [progress_hook],
                }
                if download_type == "Audio":
                    ydl_opts['postprocessors'] = [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }]
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])

            download_with_progress(video_url, download_type=download_type)
        else:
            st.write("Please enter a valid YouTube video URL.")
    except Exception as e:
        st.error(f"An error occurred: {e}")