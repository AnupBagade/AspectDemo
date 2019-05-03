"""
    This module consists of testcases to perform actions on users
    endpoint with different sets of data.
    endpoint: https://reqres.in/api/users
"""
from endpoints.user_endpoint import UserEndpoint
from test_data import user_testcase_data
import unittest


class UserTestCases(unittest.TestCase):
    """
        This class consists testcases to validate users endpoints against
        different sets of data.
    """
    @classmethod
    def setUpClass(cls):
        cls.users_url = user_testcase_data['users_url']
        cls.users_url_with_page = user_testcase_data['users_url_with_page']
        cls.users_list_keys = user_testcase_data['users_list_keys']
        cls.specific_user_url = user_testcase_data['specific_user_url']
        cls.specific_user_data = user_testcase_data['specific_user_data']
        cls.invalid_specific_user_url = user_testcase_data['invalid_specific_user_url']
        cls.create_payload = user_testcase_data['create_payload']
        cls.update_payload = user_testcase_data['update_payload']
        cls.patch_payload = user_testcase_data['patch_payload']

    def test_get_users_list(self):
        """
        Request for users list and validate status code, user related data fields
        and number of user data matching with data count.
        :return: None
        """
        resp_obj = UserEndpoint.get_user_list(self.users_url)
        self.assertEqual(resp_obj['resp_obj'].status_code, 200, 'Invalid URL - {}'.format(self.users_url))
        self.assertGreater(len(resp_obj['resp_data']['data']), 0, 'No user exists in the database.')
        user_keys = list(resp_obj['resp_data']['data'][0].keys())
        self.assertEqual(self.users_list_keys, user_keys, 'users key values is not matching with expected values.')
        self.assertEqual(int(resp_obj['resp_data']['per_page']), len(resp_obj['resp_data']['data']),
                         'Number of user entires are not matching with per page count.')

    def test_get_users_list_page(self):
        """
        Request for users list on the basis of page number and validate status code.
        :return: None
        """
        resp_obj = UserEndpoint.get_user_list(self.users_url_with_page)
        self.assertEqual(resp_obj['resp_obj'].status_code, 200, 'Invalid URL - {}'.format(self.users_url_with_page))

    def test_retrieve_specific_user(self):
        """
        Request for specific user and validate status code and data.
        :return:None
        """
        resp_obj = UserEndpoint.get_user_list(self.specific_user_url)
        self.assertEqual(resp_obj['resp_obj'].status_code, 200, 'Invalid url - {}'.format(self.specific_user_url))
        self.assertEqual(resp_obj['resp_data']['data'], self.specific_user_data,
                         'Retrieved data is not matching with expected data.')

    def test_retrieve_invalid_user(self):
        """
        Request for invalid user by passing invalid user id and validate status code.
        :return: None
        """
        resp_obj = UserEndpoint.get_user_list(self.invalid_specific_user_url)
        self.assertEqual(resp_obj['resp_obj'].status_code, 404,'Validate endpoint action with non existing user id.')

    def test_create_new_user(self):
        """
        Create new user. validate status code and user fields in POST request and response.
        :return: None
        """
        resp_obj = UserEndpoint.create_user(self.users_url, payload=self.create_payload)
        self.assertEqual(resp_obj['resp_obj'].status_code, 201, 'User creation is not successfull. '
                                                                'Please validate url and data format')
        self.assertEqual(resp_obj['resp_data']['name'], self.create_payload['name'],
                         'user name in request and response is not matching with each other.')
        self.assertEqual(resp_obj['resp_data']['job'], self.create_payload['job'],
                         'user job in request and response is not matching with each other.')
        self.assertTrue(resp_obj['resp_data']['id'].isdigit(), 'user id does not contains only numbers.')

    def test_update_existing_user(self):
        """
        Update existing user with new user data.
        Validate status code and user fields in response and request object.
        :return:None
        """
        resp_obj = UserEndpoint.update_user(self.specific_user_url, payload=self.update_payload)
        self.assertEqual(resp_obj['resp_obj'].status_code, 201,
                         'Updating user is not successful. Please validate URL and request body.')
        self.assertEqual(resp_obj['resp_data']['name'], self.update_payload['name'],
                         'user name in request and response is not matching with each other.')
        self.assertEqual(resp_obj['resp_data']['job'], self.update_payload['job'],
                         'user job in request and response is not matching with each other.')

    def test_patch_existing_user(self):
        """
        Update part of user data through patch request.
        Validate status code, new user data in both request and response objects.
        :return:None
        """
        resp_obj = UserEndpoint.patch_user(self.specific_user_url, payload=self.patch_payload)
        self.assertEqual(resp_obj['resp_obj'].status_code, 200,
                         'Updating user is not successful. Please validate URL and request body.')
        self.assertEqual(resp_obj['resp_data']['name'], self.patch_payload['name'],
                         'user name in request and response is not matching with each other.')

    def test_delete_existing_user(self):
        """
        Since data is not getting saved to database. Unable to pass newly created user id for delete operation.
        Hence testing is performed for user with id = 2.
        :return: None
        """
        resp_obj = UserEndpoint.delete_user(self.specific_user_url)
        self.assertEqual(resp_obj['resp_obj'].status_code, 204,
                         'Deleting user is not successful. Please validate URL and request body.')

    @classmethod
    def tearDownClass(cls):
        pass


