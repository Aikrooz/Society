import requests

url = 'http://127.0.0.1:8000/users/register/'
data = {
    "first_name": "Joe",
    "last_name": "Doe",
    "email": "johl.doe2@example.com",
    "username": "johlhdoe1234",
    "account_number": "1234567890",
    "age": 25,
    "password": "securePassword123",
    "confirm_password": "securePassword123"
}

response = requests.post(url, json=data)
print(f"Status Code: {response.status_code}")
try:
    print(response.json())
except requests.exceptions.JSONDecodeError:
    print("Response is not JSON:")
    print(response.text)