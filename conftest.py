import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def setup_driver(request):
    moon_url = "http://localhost:4444/wd/hub"
    url, browser, version, os = request.param
    assert os in ["linux", "mac", "windows"]
    assert browser in ["firefox", "edge", "safari", "chrome"]
    # if version is None:
    #     version = "latest"

    match browser:
        case "firefox":
            options = webdriver.FirefoxOptions()
            headless = "--headless"
        case "edge":
            options = webdriver.EdgeOptions()
            headless = "--headless=new"
        case "chrome":
            options = webdriver.ChromeOptions()
            headless = "--headless=new"
        case _:
            options = webdriver.ChromeOptions()
            headless = "--headless=new"

    options.add_argument("--no-sandbox")
    options.add_argument(headless)
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    options.set_capability("browserName", browser)
    # options.set_capability("version", version)
    options.set_capability("platformName", os)

    driver = webdriver.Remote(command_executor=moon_url, options=options)
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()
