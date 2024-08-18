""" This module contains base methods for the API """

import requests
import json


def load_token(config_file):
    with open(config_file, 'r') as file:
        config = json.load(file)
    return config['API_TOKEN']


class BaseAPI:
    """ Base API class """
    def __init__(self, base_url, config_file='config.json'):
        """ Constructor """
        self.base_url = base_url
        self.token = load_token(config_file)
        self.headers = {'Authorization': f'Bearer {self.token}',
                        'Content-Type': 'application/json'}

    def _get_headers(self):
        """ Return headers for the request """
        return self.headers

    def get(self, endpoint, params=None, timeout=10):
        """ Get method """
        url = f'{self.base_url}/{endpoint}'
        return requests.get(url, headers=self._get_headers(),
                            params=params, timeout=timeout)

    def post(self, endpoint, data, timeout=10):
        """ Post method """
        url = f'{self.base_url}/{endpoint}'
        return requests.post(url, headers=self._get_headers(),
                             json=data, timeout=timeout)

    def put(self, endpoint, data, timeout=10):
        """ Put method """
        url = f'{self.base_url}/{endpoint}'
        return requests.put(url, headers=self._get_headers(),
                            json=data, timeout=timeout)

    def delete(self, endpoint, timeout=10):
        """ Delete method """
        url = f'{self.base_url}/{endpoint}'
        return requests.delete(url, headers=self._get_headers(),
                               timeout=timeout)
