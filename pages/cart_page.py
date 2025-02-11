from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):
    def should_be_empty_cart(self):
        assert self.is_not_element_present(CartPageLocators.CART_FORMSET) == True, "Cart is not empty"

    def should_be_empty_cart_message(self):
        assert self.is_element_present(*CartPageLocators.EMPTY_CART_MESSAGE) == True, \
            "Empty cart message is not presented"
