

import requests

user_data = {
    "email": "de.ridder.harold@gmail.com",
    "password": "azertyuiop"
}

print("Sending POST request...")
response = requests.post("http://localhost:8000/users/", json=user_data)
print("Response received:", response.text)
