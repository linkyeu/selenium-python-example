from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.simple_form_demo_page import SimpleFormDemoPage


class SeleniumPlayground(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_section(self, section_name: str) -> None:
        section = By.XPATH, f"//a[contains(text(), '{section_name}')]"
        self.click(section)

    def open_simple_form_demo(self):
        self.open_section("Simple Form Demo")
        return SimpleFormDemoPage(self.driver)
