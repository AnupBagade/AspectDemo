user_testcase_data = {
    'users_url': 'https://reqres.in/api/users',
    'users_url_with_page': 'https://reqres.in/api/users?page=2',
    'users_list_keys': ['id', 'first_name', 'last_name', 'avatar'],
    'specific_user_url': 'https://reqres.in/api/users/2',
    'specific_user_data': {'id': 2, 'first_name': 'Janet', 'last_name': 'Weaver',
                           'avatar': 'https://s3.amazonaws.com/uifaces/faces/twitter/josephstein/128.jpg'},
    'invalid_specific_user_url': 'https://reqres.in/api/users/100',
    'create_payload': {'name': 'John Smith', 'job': 'Automation Engineer'},
    'update_payload': {'name': 'John Richard Smith', 'job': 'Test Automation Engineer'},
    'patch_payload': {'name': 'John Smith'},
}

register_login_testcase_data = {
    'login_url': 'https://reqres.in/api/login',
    'login_valid_payload': {'email': 'peter@klaven', 'password': 'cityslicka'},
    'login_invalid_payload': {'email': 'peter@klaven'},
    'login_blank_username': {'email': '', 'password': 'cityslicka'},
    'login_blank_password': {'email': 'peter@klaven', 'password': ''},
    'login_blank_payload': {},
    'login_extra_fields': {'email': 'peter@klaven', 'password': 'cityslicka',
                           'username': 'Testuser'},
    'register_url': 'https://reqres.in/api/register',
    'register_valid_payload': {'email': 'sydney@fife', 'password': 'pistol'},
    'register_invalid_payload': {'email': 'sydney@fife'},
    'register_blank_username': {'email': '', 'password': 'pistol'},
    'register_blank_password': {'email': 'sydney@fife', 'password': ''},
    'register_blank_payload': {},
    'register_extra_fields': {'email': 'sydney@fife', 'password': 'pistol',
                              'username': 'newuser'}

}

resource_testcase_data = {
    'list_resource_url': 'https://reqres.in/api/unknown',
    'single_resource_url': 'https://reqres.in/api/unknown/2',
    'invalid_resource_url': 'https://reqres.in/api/unknown/100',
    'single_resource_data': {'name': 'fuchsia rose'},
    'resources_list_keys': {'id', 'name', 'color', 'year', 'pantone_value'},
    'default_endpoint': 'https://reqres.in/api/randomstring'
}

