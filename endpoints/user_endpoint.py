"""
    This module deals with CRUD operations on users endpoint.
    endpoint: https://reqres.in/api/users
"""
import json
import requests


class UserEndpoint:
    """This is a class consisting of functions to perform action on user endpoints."""

    @staticmethod
    def get_user_list(url):
        """
        Request for single/multiple users data.
        :param url: users endpoint.
        :return: None
        """
        resp = requests.get(url)
        resp_obj = {
            'resp_obj': resp,
            'resp_data': json.loads(resp.text)
        }
        return resp_obj

    @staticmethod
    def create_user(url, payload):
        """
        POST request to create user with provided user data and endpoint.
        :param url: users endpoint.
        :param payload: user data.
        :return:None
        """
        resp = requests.post(url, data=payload)
        resp_obj = {
            'resp_obj': resp,
            'resp_data': json.loads(resp.text)
        }
        return resp_obj

    @staticmethod
    def update_user(url, payload):
        """
        PUT request to update existing user data with new user data.
        :param url: users endpoint.
        :param payload: new user data.
        :return:None
        """
        resp = requests.post(url, data=payload)
        resp_obj = {
            'resp_obj': resp,
            'resp_data': json.loads(resp.text)
        }
        return resp_obj

    @staticmethod
    def patch_user(url, payload):
        """
        PATCH request to update part of existing user data with new user data.
        :param url: users endpoint.
        :param payload: new user data.
        :return: None
        """
        resp = requests.patch(url, data=payload)
        resp_obj = {
            'resp_obj': resp,
            'resp_data': json.loads(resp.text)
        }
        return resp_obj

    @staticmethod
    def delete_user(url):
        """
        DELETE request to delete existing user.
        :param url: users endpoint.
        :return: None
        """
        resp = requests.delete(url)
        resp_obj = {
            'resp_obj': resp
        }
        return resp_obj
