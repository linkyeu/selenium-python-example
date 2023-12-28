import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utilities.test_data import TestData


@pytest.fixture(params=["chrome", "firefox", "edge"])
def setup_driver(request):
    if request.param == "chrome":
        option = webdriver.ChromeOptions()
        option.add_argument("--headless=new")
        option.add_argument("--disable-gpu")
        driver = webdriver.Chrome(options=option)

    elif request.param == "firefox":
        option = webdriver.FirefoxOptions()
        option.add_argument("--headless")
        option.add_argument("--disable-gpu")
        driver = webdriver.Firefox(options=option)

    elif request.param == "edge":
        option = webdriver.FirefoxOptions()
        option.add_argument("--headless")
        option.add_argument("--disable-gpu")
        driver = webdriver.Edge(options=option)

    driver.get("https://www.lambdatest.com/selenium-playground")
    driver.maximize_window()
    yield driver
    driver.quit()
