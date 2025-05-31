import requests

# Define the API endpoint and your API key
API_URL = "https://api.openai.com/v1/chat/completions"
API_KEY = ""

# Set up the headers
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

# Define the payload
payload = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello, how can you assist me?"}
    ],
    "max_tokens": 1000
}

# Make the POST request
response = requests.post(API_URL, headers=headers, json=payload)

# Check the response
if response.status_code == 200:
    print("Response:", response.json())
else:
    print("Error:", response.status_code, response.text)