import requests

# Define the API endpoint
url = "https://api.example.com/resource"

# Define the parameters and headers
params = {
    "id": 12345,  # Replace with the desired ID
    "query": "example"
}
headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",  # Replace with your access token
    "Content-Type": "application/json"
}

# Make the GET request
response = requests.get(url, params=params, headers=headers)

# Check the response status and print the result
if response.status_code == 200:
    print("Response Data:", response.json())
else:
    print(f"Failed to fetch data. Status Code: {response.status_code}, Error: {response.text}")