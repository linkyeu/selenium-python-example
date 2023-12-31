import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
# driver = webdriver.Edge(EdgeChromiumDriverManager().install())


@pytest.fixture()
def setup_driver(request):
    url = request.param
    option = webdriver.ChromeOptions()
    option.add_argument("--no-sandbox")
    option.add_argument("--headless=new")
    option.add_argument("--disable-gpu")
    option.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=option,
    )
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()
