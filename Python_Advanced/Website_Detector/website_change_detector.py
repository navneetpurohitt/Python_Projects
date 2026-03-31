import os
import time
import smtplib
import hashlib
import requests
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuration
URL = "https://example.com"  # Replace with the URL you want to monitor
CHECK_INTERVAL = 3600  # Time interval in seconds (e.g., 1 hour)
EMAIL_SENDER = os.getenv("EMAIL_SENDER")  # Sender email (use environment variable)
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")  # Sender email password (use environment variable)
EMAIL_RECEIVER = "receiver@example.com"  # Receiver email

# Function to fetch webpage content
def fetch_webpage(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching webpage: {e}")
        return None

# Function to hash webpage content
def hash_content(content):
    return hashlib.sha256(content.encode("utf-8")).hexdigest()

# Function to send email notification
def send_email(subject, body):
    try:
        msg = MIMEMultipart()
        msg["From"] = EMAIL_SENDER
        msg["To"] = EMAIL_RECEIVER
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.send_message(msg)
        print("Email notification sent.")
    except Exception as e:
        print(f"Error sending email: {e}")

# Main function
def monitor_website():
    previous_hash = None

    while True:
        print("Checking website for changes...")
        content = fetch_webpage(URL)
        if content:
            current_hash = hash_content(content)

            if previous_hash and current_hash != previous_hash:
                print("Change detected!")
                send_email(
                    subject="Website Change Detected",
                    body=f"The content of the website {URL} has changed."
                )
            else:
                print("No changes detected.")

            previous_hash = current_hash

        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    monitor_website()