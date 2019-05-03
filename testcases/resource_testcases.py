"""
    This module consists of testcases to perform read actions on unknown
    endpoint with different sets of data.
    endpoint: https://reqres.in/api/unknown
"""
from endpoints.resources_endpoint import ResourceEndpoint
from test_data import resource_testcase_data
import unittest


class ResourceTestCases(unittest.TestCase):
    """
        This class consists testcases to validate resources endpoints against
        different sets of data.
    """
    @classmethod
    def setUpClass(cls):
        cls.list_resource_url = resource_testcase_data['list_resource_url']
        cls.single_resource_url = resource_testcase_data['single_resource_url']
        cls.invalid_resource_url = resource_testcase_data['invalid_resource_url']
        cls.resources_list_keys = resource_testcase_data['resources_list_keys']
        cls.default_endpoint = resource_testcase_data['default_endpoint']

    def test_get_list_resource(self):
        """
        Request for unknown endpoint and validate list of resources are returned.
        If list of users are returned, then keys in response object are matched with expected data.
        If list is empty then list count is matched with per_page count.
        :return:None
        """
        resp_obj = ResourceEndpoint.get_resource(self.list_resource_url)
        self.assertEqual(resp_obj['resp_obj'].status_code, 200,
                         'Unable to retrieve resources list or status code mismatch.'
                         ' Please validate URL.')
        if len(resp_obj['resp_data']['data']) > 0:
            resource_list_keys = set(resp_obj['resp_data']['data'][0].keys())
            self.assertEqual(self.resources_list_keys, resource_list_keys,
                             'Resource keys present in response data is not matching with expected')
        else:
            self.assertEqual(resp_obj['resp_data']['per_page'], 0,
                             ' Resources count is not matching with per page count.')

    def test_get_single_resource(self):
        """
        Request for single resource from unknown endpoint.
        Validate status code and name value of user in response object.
        :return: None
        """
        resp_obj = ResourceEndpoint.get_resource(self.single_resource_url)
        self.assertEqual(resp_obj['resp_obj'].status_code, 200,
                         'Unable to retrieve specific resource or status code mismatch.'
                         ' Please validate URL.')
        self.assertEqual(resp_obj['resp_data']['data']['name'], resource_testcase_data['single_resource_data']['name'])

    def test_get_invalid_resource(self):
        """
        Request for invalid resource from unknown endpoint. Validate status code.
        :return:
        """
        resp_obj = ResourceEndpoint.get_resource(self.invalid_resource_url)
        self.assertEqual(resp_obj['resp_obj'].status_code, 404)

    def test_default_endpoint(self):
        """
        Make request with random string attached to https://reqres.in/api/. This will be the default endpoint.
        :return:None
        """
        resp_obj = ResourceEndpoint.get_resource(self.default_endpoint)
        self.assertEqual(resp_obj['resp_obj'].status_code, 200)



    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main()