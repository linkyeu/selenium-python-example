import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def setup_driver(request):
    url = request.param
    option = webdriver.ChromeOptions()
    option.add_argument("--headless=new")
    option.add_argument("--disable-gpu")
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=option,
    )
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()
