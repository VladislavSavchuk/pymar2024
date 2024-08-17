""" This module contains constants used in the tests """


""" This module contains constants used in the tests """
BASE_URL = 'https://alexqa.netlify.app/.netlify/functions'
TOKEN = ("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQ"
         "iOiIxMTAxMzY2ODg5ODMxNzQ0OTczMjAiLCJpYXQiOjE3MjM"
         "4OTY2MDUsImV4cCI6MTcyMzkwMDIwNX0.yOcB8XBzUABj5Tg-"
         "ytnI2lPa8gqmwvsjS_gNR1JMjoE")

HEADERS = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {TOKEN}'
}

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
