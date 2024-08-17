""" This module contains base methods for the API """

import requests
from homework.homework27.conftest import HEADERS


class BaseAPI:
    """ Base API class """
    def __init__(self, base_url):
        """ Constructor """
        self.base_url = base_url
        self.headers = HEADERS

    def get(self, endpoint, params=None):
        """ Get method """
        url = f'{self.base_url}/{endpoint}'
        return requests.get(url, headers=self.headers, params=params)

    def post(self, endpoint, data):
        """ Post method """
        url = f'{self.base_url}/{endpoint}'
        return requests.post(url, headers=self.headers, json=data)

    def put(self, endpoint, data):
        """ Put method """
        url = f'{self.base_url}/{endpoint}'
        return requests.put(url, headers=self.headers, json=data)

    def delete(self, endpoint):
        """ Delete method """
        url = f'{self.base_url}/{endpoint}'
        return requests.delete(url, headers=self.headers)