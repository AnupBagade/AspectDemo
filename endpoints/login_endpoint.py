"""
    This module deals with login operations on login endpoint.
    endpoint: https://reqres.in/api/login
"""
import json
import requests


class LoginEndpoint:
    """This is a class perform login related operations on login endpoint."""

    @staticmethod
    def login_user(url, payload):
        """
        Login user with provided payload and endpoint.
        :param url: login endpoint.
        :param payload: credentials for login.
        :return: None.
        """
        resp = requests.post(url, data=payload)
        resp_obj = {
            'resp_obj': resp,
            'resp_data': json.loads(resp.text)
        }
        return resp_obj
