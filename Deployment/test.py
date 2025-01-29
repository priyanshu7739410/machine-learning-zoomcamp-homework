import requests

client = {"job": "student", "duration": 280, "poutcome": "failure"}

response = requests.post('http://localhost:9696/load', json=client).json()
print("Received response:", response)  # Debugging line
