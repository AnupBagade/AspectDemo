"""
    This module deals with reading operations on unknown endpoint.
    endpoint: https://reqres.in/api/unknown
"""
import json
import requests


class ResourceEndpoint:
    """This is a class perform reading operations on unknown endpoint."""

    @staticmethod
    def get_resource(url):
        """
        Request for resource from provided endpoint.
        :param url: unknown endpoint.
        :return: None.
        """
        resp = requests.get(url)
        resp_obj = {
            'resp_obj': resp,
            'resp_data': json.loads(resp.text)
        }
        return resp_obj
