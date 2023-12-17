import pytest
from selenium import webdriver


class LoadableComponent:
    pass


@pytest.fixture(scope="function")
def driver():
    URL = "https://demoqa.com/"
    driver = webdriver.Chrome()
    driver.get(URL)
    driver.implicitly_wait(3)
    driver.maximize_window()
    assert driver.current_url == URL
    yield driver
    driver.quit()
