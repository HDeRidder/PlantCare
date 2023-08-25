import pytest
import requests

# Define the base URL of your FastAPI server
BASE_URL = "http://127.0.0.1:8000"

# Helper function to get an access token
def get_access_token():
    form_data = {
        "username": "test@gmail.com",
        "password": "test123"
    }
    response = requests.post(f"{BASE_URL}/token", data=form_data)
    assert response.status_code == 200
    return response.json()["access_token"]


# Test the /users/me endpoint with authentication
def test_read_users_me():
    access_token = get_access_token()
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get(f"{BASE_URL}/users/me", headers=headers)
    assert response.status_code == 200
    assert response.json() is not None

# Test the /users/ endpoint with authentication
def test_read_users():
    access_token = get_access_token()
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get(f"{BASE_URL}/users/", headers=headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Test the /users/{user_id} endpoint with authentication
def test_read_user():
    access_token = get_access_token()
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    # Replace {user_id} with an existing user ID
    user_id = 2
    response = requests.get(f"{BASE_URL}/users/{user_id}", headers=headers)
    assert response.status_code == 200
    assert response.json() is not None

# Test the /plantreminders/ endpoint
def test_read_plantreminders():
    response = requests.get(f"{BASE_URL}/plantreminders/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Test the /plantreminders/lighting/ endpoint
def test_read_plantreminders_by_lighting():
    # Replace {lighting} with an existing lighting value
    lighting = "Full Sun"
    response = requests.get(f"{BASE_URL}/plantreminders/lighting/?lighting={lighting}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Test the /plantreminders/watering/ endpoint
def test_read_plantreminders_by_watering():
    # Replace {watering} with an existing watering value
    watering = "Once a week"
    response = requests.get(f"{BASE_URL}/plantreminders/watering/?watering={watering}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Test the /users/ POST endpoint
def test_create_user():
    data = {
        "email": "newuser@gmail.com",
        "password": "newuserpass"
    }
    response = requests.post(f"{BASE_URL}/users/", json=data)
    assert response.status_code == 200
    assert response.json()["email"] == "newuser@gmail.com"

# Test the /users/{user_id} PUT endpoint
def test_update_user():
    access_token = get_access_token()
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    user_id = 3 # Replace with an existing user ID
    data = {
        "email": "updateduser@gmail.com"
    }
    response = requests.put(f"{BASE_URL}/users/{user_id}", headers=headers, json=data)
    assert response.status_code == 200
    assert response.json()["email"] == "updateduser@gmail.com"

# Test the /users/{user_id} DELETE endpoint
def test_delete_user():
    access_token = get_access_token()
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    user_id = 1  # Replace with an existing user ID
    response = requests.delete(f"{BASE_URL}/users/{user_id}", headers=headers)
    assert response.status_code == 200
    assert response.json()["email"] == "updateduser@gmail.com"  # Adjust based on your response structure


# Test the /plantreminders/{plantreminder_id} DELETE endpoint
def test_delete_plantreminder():
    access_token = get_access_token()
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    plantreminder_id = 1  # Replace with an existing plantreminder ID
    response = requests.delete(f"{BASE_URL}/plantreminders/{plantreminder_id}", headers=headers)
    assert response.status_code == 200
    assert response.json()["id"] == plantreminder_id  # Adjust based on your response structure

# ... (other test functions for other endpoints)

if __name__ == "__main__":
    pytest.main()
