import requests

client = {"job": "management", "duration": 400, "poutcome": "success"}

response = requests.post('http://localhost:9696/load', json=client).json()
print("Received response:", response)  # Debugging line
