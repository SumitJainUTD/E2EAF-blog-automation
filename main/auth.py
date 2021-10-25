

from main.exceptions import DataError
from api_client import ApiClient
from utils.configuration import Configuration


class Auth:
    config = Configuration("qa")

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    def __str__(self):
        return self.username

    def login(self, username, password):
        if (username is None) or (password is None):
            raise DataError("Require Username and password for login")

        url = self.config.base_uri + self.config.auth_uri
        body = {
            'username': username,
            'password': password
        }
        response = self.api_client.call_api(method="POST", url=url, body=body)
        if response.status_code == 200:
            access_token = response.json()['access']
            refresh = response.json()['refresh']
            return response.json()
        elif response.status_code == 401:
            raise DataError("Invalid username or password")

    def login(self, refresh_token):
        if refresh_token is None:
            raise DataError("refresh_token is None")

        url = self.config.base_uri + self.config.auth_uri + "refresh"
        body = {
            'refresh': refresh_token
        }
        response = self.api_client.call_api(method="POST", url=url, body=body)
        if response.status_code == 200:
            access_token = response.json()['access']
            refresh = response.json()['refresh']
            return response.json()
        elif response.status_code == 401:
            raise DataError("Invalid refresh token")
