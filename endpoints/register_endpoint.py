"""
    This module deals with login operations on login endpoint.
    endpoint: https://reqres.in/api/login
"""
import requests


class RegisterEndpoint:
    """This is a class performs user registration operations on register endpoint."""

    @staticmethod
    def register_user(url, payload):
        """
        Register user with supplied payload and endpoint.
        :param url: register endpoint.
        :param payload: credentials for registration
        :return: None
        """
        resp = requests.post(url, data=payload)
        resp_obj = {
            'resp_obj': resp,
            'resp_data': resp.json()
        }
        return resp_obj
