from selenium.webdriver.common.by import By

from pages.base_page import Page


class CartPage(Page):

    CART_EMPTY_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg'] h1")
    TOTAL_ITEMS = (By.XPATH, "//div[./span[contains(text(), 'total')]]")

    def open(self):
        self.open_url('https://www.target.com/cart')

    def verify_cart_empty(self):
        self.wait_for_element_appear(*self.CART_EMPTY_MSG)
        self.verify_text('Your cart is empty', *self.CART_EMPTY_MSG)

    def verify_cart(self, amount):
        actual_amount = self.verify_text(amount, *self.TOTAL_ITEMS)
        cart_summary = self.driver.find_element().text
        assert amount in actual_amount, f'Expected {amount} but got {cart_summary}'
    