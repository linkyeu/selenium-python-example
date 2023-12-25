from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SimpleFormDemoPage(BasePage):
    enter_message_field = (By.ID, "user-message")
    get_checked_value_btn = (By.ID, "showInput")
    your_message_text = (By.ID, "message")

    def set_message(self, message: str) -> None:
        self.set(SimpleFormDemoPage.enter_message_field, message)

    def press_get_checked_value_btn(self) -> None:
        self.click(SimpleFormDemoPage.get_checked_value_btn)

    def get_your_message(self) -> str:
        return self.get_text(SimpleFormDemoPage.your_message_text)
