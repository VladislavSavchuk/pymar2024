""" This module contains tests for the user API """

import pytest
from homework.homework27.conftest import BASE_URL, user_schema
from homework.homework27.methods.api_user_methods import \
    UserAPI, generate_random_email
from jsonschema import validate

user_api = UserAPI(BASE_URL)


@pytest.fixture
def test_user_id():
    """ Fixture for creating a new user """
    random_email = generate_random_email()
    user_data = {
        "name": "John Doe",
        "email": random_email,
        "age": 30,
        "phoneNumber": "+12345678901",
        "address": "123 Main St",
        "role": "user",
        "referralCode": "ABCDEFGH"
    }
    response = user_api.create_user(user_data)
    assert response.status_code == 200, (f'Expected 200, '
                                         f'got {response.status_code}')

    response_data = response.json()

    return response_data['id']


def test_get_user(test_user_id):
    """ Test for getting a user by ID """
    response = user_api.get_user(test_user_id)
    assert response.status_code == 200, (
        f'Expected 200, but got {response.status_code}')

    response_data = response.json()
    validate(instance=response_data, schema=user_schema)

    assert response_data["id"] == test_user_id


def test_update_user(test_user_id):
    """ Test for updating a user """
    user_data = {
        "name": "John Smith",
        "email": "johnsmith@example.com",
        "age": 31,
        "phoneNumber": "+1234567890",
        "address": "456 Elm Stanciya Zavodskaya",
        "role": "user",
        "referralCode": "ABCDEFGH"
    }

    response = user_api.update_user(test_user_id, user_data)

    assert response.status_code == 200, (
        f'Expected 200, but got {response.status_code}')

    response_data = response.json()
    validate(instance=response_data, schema=user_schema)

    assert response_data["name"] == user_data["name"], (
        f"Expected name {user_data['name']}, "
        f"but got {response_data['name']}")

    assert response_data["email"] == user_data["email"], (
        f"Expected email {user_data['email']}, "
        f"but got {response_data['email']}")


def test_get_users():
    """ Test for getting all users """
    response = user_api.get_users()
    assert response.status_code == 200, (f'Expected 200, '
                                         f'got {response.status_code}')

    response_data = response.json()

    assert isinstance(response_data, dict), (
        f"Expected response data to be a dictionary, "
        f"but got {type(response_data)}")


def test_check_user_status(test_user_id):
    """ Test for checking the status of a user """
    response = user_api.check_user_status(test_user_id)

    assert response.status_code == 200, (
        f'Expected 200, but got {response.status_code}')

    response_data = response.json()

    assert response_data['id'] == test_user_id, 'Invalid user ID'
    assert 'status' in response_data, \
        "Response JSON does not contain 'status' key"
    assert response_data['status'] == 'created', (
        f"Expected status 'created', "
        f"but got {response_data['status']}")


@pytest.mark.xfail(reason="API endpoint currently returns 404 "
                          "instead of 200")
def test_delete_user(test_user_id):
    """ Test for deleting a user """
    response = user_api.delete_user(test_user_id)

    assert response.status_code == 200, (
        f'Expected 200, but got {response.status_code}')

    response_data = response.json()
    print(response_data)

    assert response_data['id'] == test_user_id, 'Invalid user ID'
    assert response_data['status'] == 'deleted', 'Invalid status'


def test_get_non_existent_user():
    """ Test for getting a non-existent user """
    non_existent_user_id = "nonexistentid123"

    response = user_api.get_user(non_existent_user_id)

    assert response.status_code == 400, (f'Expected 400, '
                                         f'got {response.status_code}')

    response_data = response.json()

    assert "error" in response_data, \
        "Response does not contain 'error' field"
    assert response_data["error"] == "Invalid User ID format", \
        "Unexpected error message"
