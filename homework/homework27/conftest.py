""" This module contains constants used in the tests """


BASE_URL = 'https://alexqa.netlify.app/.netlify'
TOKEN = ("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9."
         "eyJ1c2VySWQiOiIxMTM1Nzk5NzYwNzcxNDUzN"
         "jQxNzMiLCJpYXQiOjE3MjM5MDE0NzMsImV4cC"
         "I6MTcyMzkwNTA3M30.MFg9EjAcnHnbifufy3F"
         "tJkDogQ8AAKDDw2W2_BBlpDw")

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
