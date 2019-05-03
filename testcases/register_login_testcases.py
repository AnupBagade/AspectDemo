"""
    This module deals with login and registration operations on login
    and user endpoint respectively.
    login_endpoint: https://reqres.in/api/login
    register_endpoint: https://reqres.in/api/register
"""
from endpoints.login_endpoint import LoginEndpoint
from endpoints.register_endpoint import RegisterEndpoint
from test_data import register_login_testcase_data
import unittest



class RegisterLoginTestCases(unittest.TestCase):
    """ This class perform login and register operations with different sets of data
        to validate endpoints response.
    """
    @classmethod
    def setUpClass(cls):
        cls.login_url = register_login_testcase_data['login_url']
        cls.login_valid_payload = register_login_testcase_data['login_valid_payload']
        cls.login_invalid_payload = register_login_testcase_data['login_invalid_payload']
        cls.login_blank_username = register_login_testcase_data['login_blank_username']
        cls.login_blank_password = register_login_testcase_data['login_blank_password']
        cls.login_blank_payload = register_login_testcase_data['login_blank_payload']
        cls.login_extra_fields = register_login_testcase_data['login_extra_fields']
        cls.register_url = register_login_testcase_data['register_url']
        cls.register_valid_payload = register_login_testcase_data['register_valid_payload']
        cls.register_invalid_payload = register_login_testcase_data['register_invalid_payload']
        cls.register_blank_username = register_login_testcase_data['register_blank_username']
        cls.register_blank_password = register_login_testcase_data['register_blank_password']
        cls.register_blank_payload = register_login_testcase_data['register_blank_payload']
        cls.register_extra_fields = register_login_testcase_data['register_extra_fields']

    def test_login_successful(self):
        """
        Login with valid credentials.
        Validate status code and token present in response data.
        :return: None
        """
        resp_obj = LoginEndpoint.login_user(self.login_url, payload=self.login_valid_payload)
        self.assertEqual(resp_obj['resp_obj'].status_code, 200)
        self.assertIn('token', resp_obj['resp_data'].keys())

    def test_login_unsuccessful(self):
        """
        Login with invalid credentials.
        Validate status code and error message exist in response.
        :return: None
        """
        resp_obj = LoginEndpoint.login_user(self.login_url, payload=self.login_invalid_payload)
        self.assertEqual(resp_obj['resp_obj'].status_code, 400)
        self.assertIn('error', resp_obj['resp_data'].keys())

    def test_login_blank_username(self):
        """
        Login with blank username and valid password.
        Validate status code and error message exist in response data.
        :return: None
        """
        resp_obj = LoginEndpoint.login_user(self.login_url, payload=self.login_blank_username)
        self.assertEqual(resp_obj['resp_obj'].status_code, 400)
        self.assertIn('error', resp_obj['resp_data'].keys())

    def test_login_blank_password(self):
        """
        Login with blank_password and valid username.
        Validate status code and error message exist in response data.
        :return: None
        """
        resp_obj = LoginEndpoint.login_user(self.login_url, payload=self.login_blank_password)
        self.assertEqual(resp_obj['resp_obj'].status_code, 400)
        self.assertIn('error', resp_obj['resp_data'].keys())

    def test_login_blank_payload(self):
        """
        Login with blank request body.
        Validate status code and error message exist in response data.
        :return: None
        """
        resp_obj = LoginEndpoint.login_user(self.login_url, payload=self.login_blank_payload)
        self.assertEqual(resp_obj['resp_obj'].status_code, 400)
        self.assertIn('error', resp_obj['resp_data'].keys())

    def test_login_with_extra_fields(self):
        """
        Login with extra fields.
        Validate status code.
        :return:None
        """
        resp_obj = LoginEndpoint.login_user(self.login_url, payload=self.login_extra_fields)
        self.assertEqual(resp_obj['resp_obj'].status_code, 200)
        self.assertIn('token', resp_obj['resp_data'].keys())

    def test_register_successful(self):
        """
        Register with valid data format.
        Validate status code and token present in response.
        :return:None
        """
        resp_obj = RegisterEndpoint.register_user(self.register_url, payload=self.register_valid_payload)
        self.assertEqual(resp_obj['resp_obj'].status_code, 201)
        self.assertIn('token', resp_obj['resp_data'].keys())

    def test_register_unsuccessful(self):
        """
        Register with invalid data format.
        Validate status code and error message present in response.
        :return: None
        """
        resp_obj = RegisterEndpoint.register_user(self.register_url, payload=self.register_invalid_payload)
        self.assertEqual(resp_obj['resp_obj'].status_code, 400)
        self.assertIn('error', resp_obj['resp_data'].keys())

    def test_register_blank_username(self):
        """
        Register with blank username and valid password.
        Validate status code and error message present in response.
        :return: None
        """
        resp_obj = RegisterEndpoint.register_user(self.register_url, payload=self.register_blank_username)
        self.assertEqual(resp_obj['resp_obj'].status_code, 400)
        self.assertIn('error', resp_obj['resp_data'].keys())

    def test_register_blank_password(self):
        """
        Register with blank password and valid username.
        Validate status code and error message present in response.
        :return: None
        """
        resp_obj = RegisterEndpoint.register_user(self.register_url, payload=self.register_blank_password)
        self.assertEqual(resp_obj['resp_obj'].status_code, 400)
        self.assertIn('error', resp_obj['resp_data'].keys())

    def test_register_blank_payload(self):
        """
        Register with blank request body.
        Validate status code and error message present in response.
        :return:None
        """
        resp_obj = RegisterEndpoint.register_user(self.register_url, payload=self.register_blank_payload)
        self.assertEqual(resp_obj['resp_obj'].status_code, 400)
        self.assertIn('error', resp_obj['resp_data'].keys())

    def test_register_with_extra_fields(self):
        """
        Register with extra fields in request body.
        Validate status code and error message present in response.
        :return: None
        """
        resp_obj = RegisterEndpoint.register_user(self.register_url, payload=self.register_extra_fields)
        self.assertEqual(resp_obj['resp_obj'].status_code, 201)
        self.assertIn('token', resp_obj['resp_data'].keys())

    @classmethod
    def tearDownClass(cls):
        pass
