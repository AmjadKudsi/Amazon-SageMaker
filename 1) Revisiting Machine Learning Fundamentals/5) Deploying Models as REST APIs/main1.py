import requests

# API endpoint URL for the FastAPI server
url = "http://localhost:8000"

# Try to send a GET request to the server to check if it's running
try:
    response = requests.get(url)
    # If we get any response, the server is up and reachable
    print("Server is running at http://localhost:8000")
except requests.exceptions.ConnectionError:
    # This error occurs if the server is not running or not reachable
    print("Error: Could not connect to API. Make sure the server is running on localhost:8000")
except Exception as e:
    # Catch any other unexpected errors and print the error message
    print(f"Error: {e}")