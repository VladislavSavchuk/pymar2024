""" This module contains base methods for the API """

import requests
from homework.homework27.conftest import HEADERS


class BaseAPI:
    """ Base API class """
    def __init__(self, base_url):
        """ Constructor """
        self.base_url = base_url
        self.headers = HEADERS

    def get(self, endpoint, params=None, timeout=10):
        """ Get method """
        url = f'{self.base_url}/{endpoint}'
        return requests.get(url, headers=self.headers,
                            params=params, timeout=timeout)

    def post(self, endpoint, data, timeout=10):
        """ Post method """
        url = f'{self.base_url}/{endpoint}'
        return requests.post(url, headers=self.headers,
                             json=data, timeout=timeout)

    def put(self, endpoint, data, timeout=10):
        """ Put method """
        url = f'{self.base_url}/{endpoint}'
        return requests.put(url, headers=self.headers,
                            json=data, timeout=timeout)

    def delete(self, endpoint, timeout=10):
        """ Delete method """
        url = f'{self.base_url}/{endpoint}'
        return requests.delete(url, headers=self.headers,
                               timeout=timeout)
