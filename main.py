from testcases import user_testcases, register_login_testcases, resource_testcases
from HtmlTestRunner import HTMLTestRunner
from unittest import TestLoader, TestSuite


def main():
    """
    Import all testcases and create test_suite object.
    Pass test_suite object to run method of HTMLTestRunner object.
    :return:None
    """
    testcases_user = TestLoader().loadTestsFromTestCase(user_testcases.UserTestCases)
    testcases_register_login = TestLoader().loadTestsFromTestCase(register_login_testcases.RegisterLoginTestCases)
    testcases_resources = TestLoader().loadTestsFromTestCase(resource_testcases.ResourceTestCases)
    test_suite = TestSuite([testcases_user, testcases_register_login, testcases_resources])
    runner = HTMLTestRunner(output=r'C:\aspect_demo\AspectDemo\Reports', combine_reports=True)
    runner.run(test_suite)


if __name__ == '__main__':
    main()