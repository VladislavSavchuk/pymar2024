""" This module contains methods for the user API """

import uuid
from homework.homework27.methods.api_base_methods import BaseAPI


def generate_random_email():
    """ Generate random email """
    unique_id = uuid.uuid4()
    random_email = f"user_{unique_id}@example.com"
    return random_email


class UserAPI(BaseAPI):
    """ User API class """
    def __init__(self, base_url):
        """ Constructor """
        super().__init__(base_url)
        self.user_endpoint = '/functions/'

    def create_user(self, user_data):
        """ Create user """
        return self.post(f'{self.user_endpoint}createUser', user_data)

    def get_user(self, user_id):
        """ Get user by ID """
        return self.get(f'{self.user_endpoint}getUser/{user_id}')

    def update_user(self, user_id, user_data):
        """ Update user """
        return self.put(f'{self.user_endpoint}updateUser/{user_id}',
                        user_data)

    def delete_user(self, user_id):
        """ Delete user """
        return self.delete(f'{self.user_endpoint}deleteUser/{user_id}')

    def check_user_status(self, user_id):
        """ Check user status """
        return self.get(f'{self.user_endpoint}checkUserStatus/{user_id}')

    def get_users(self, page=1, limit=10):
        """ Get users """
        params = {'page': page, 'limit': limit}
        return self.get(f'{self.user_endpoint}getUsers', params=params)
