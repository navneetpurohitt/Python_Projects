import requests

def fetch_api_data(url):
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Error: Received status code {response.status_code}")
            return None
        else:
            print("Request was successful.")
            response.raise_for_status()  # Raise an HTTPError for bad responses
            return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/posts"  # Example API URL
    data = fetch_api_data(api_url)
    if data:
 
        for i in data:
          
            for j,k in i.items():
                print(f"J: {j}: K: {k}")