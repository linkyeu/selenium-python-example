from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.drag_and_drop_page import DragAndDropPage
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

    # def open_drag_and_drop(self):
    #     self.open_section("Drag & Drop Sliders")
    #     return DragAndDropPage(self.driver)
