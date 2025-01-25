from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_cart(self):
        self.should_be_add_to_cart_button()
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()
        self.solve_quiz_and_get_code()

    def should_be_correct_confirm_message(self):
        self._should_be_confirm_message()
        self._should_be_correct_product_name()

    def should_cart_total_be_equal_to_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        cart_total = self.browser.find_element(*ProductPageLocators.CART_TOTAL)
        assert product_price.text == cart_total.text, "Cart total and the added product price are not equal"

    def should_be_add_to_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BUTTON), "Add to cart button is not presented"

    def _should_be_confirm_message(self):
        assert self.is_element_present(*ProductPageLocators.CONFIRM_MESSAGE), "Confirm message is not presented"
        confirm_message = self.browser.find_element(*ProductPageLocators.CONFIRM_MESSAGE)
        assert confirm_message.text.endswith(" has been added to your basket."), "Confirm message is incorrect"

    def _should_be_correct_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        confirm_message = self.browser.find_element(*ProductPageLocators.CONFIRM_MESSAGE)
        assert confirm_message.text.startswith(product_name.text), ("Product name in confirm message doesn't match "
                                                                    "the product added")
