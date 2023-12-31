import pytest
import allure

from pages.login_page import LoginPage
from utilities.test_data import TestData


class TestLogin:

    @allure.epic("TestLogin: ID0001")
    @pytest.mark.parametrize(
        "setup_driver", ["https://ecommerce-playground.lambdatest.io/index.php?route=account/login"], True,
    )
    def test_valid_credentials(self, setup_driver):
        login_page = LoginPage(setup_driver)
        login_page.set_email_address(TestData.email)
        login_page.set_password(TestData.password)
        login_page.click_login_button()
        actual_title = login_page.get_title()
        assert actual_title == "My Account"

    @allure.epic("TestLogin: ID0002")
    @pytest.mark.parametrize(
        "setup_driver", ["https://ecommerce-playground.lambdatest.io/index.php?route=account/login"], True,
    )
    def test_invalid_credentials(self, setup_driver):
        login_page = LoginPage(setup_driver)
        login_page.log_into_application(
            "Invalid Email", "Invalid Password"
        )
        actual_message = login_page.get_warning_message()
        assert actual_message.__contains__("Warning")
