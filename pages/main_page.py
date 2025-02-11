from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def go_to_cart(self):
        go_to_cart_button = self.browser.find_element(*MainPageLocators.GO_TO_CART_BUTTON)
        go_to_cart_button.click()
