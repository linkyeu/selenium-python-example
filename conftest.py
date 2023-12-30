import pytest
from selenium import webdriver


@pytest.fixture()
def setup_driver(request):
    url = request.param
    option = webdriver.ChromeOptions()
    option.add_argument("--headless=new")
    option.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=option)
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()
