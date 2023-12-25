import pytest
from selenium import webdriver

from pages.selenium_playground import SeleniumPlayground
from utilities.test_data import TestData


def test_simple_form_demo(setup_driver):
    driver = setup_driver
    playground_page = SeleniumPlayground(driver)
    demo_page = playground_page.open_simple_form_demo()
    assert driver.current_url.__contains__("simple-form-demo")

    expected_text = "Welcome to LambdaTest"
    demo_page.set_message(expected_text)
    demo_page.press_get_checked_value_btn()
    actual_text = demo_page.get_your_message()
    assert expected_text == actual_text
