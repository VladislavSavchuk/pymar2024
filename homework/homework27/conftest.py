""" This module contains constants used in the tests """


BASE_URL = 'https://alexqa.netlify.app/.netlify'

user_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "name": {"type": "string"},
        "email": {"type": "string"},
        "age": {"type": "number"},
        "phoneNumber": {"type": "string"},
        "address": {"type": "string"},
        "role": {"type": "string"},
        "referralCode": {"type": ["string", "null"]},
        "status": {"type": "string"},
        "createdAt": {"type": "string"},
        "createdBy": {"type": "string"}
    },
    "required": ["id", "name", "email", "age",
                 "phoneNumber", "address", "role"]
}
