from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class MainPage(Page):
    SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCartButton']")
    SIDE_NAV_SIGN_IN_BTN = (By.CSS_SELECTOR, "[data-test='accountNav-signIn']")

    def open(self):
        self.open_url('https://www.target.com/')

    def side_window_signin_btn(self):
        self.driver.find_element(*self.SIDE_NAV_SIGN_IN_BTN).click()

    def side_nav_click_add_to_cart(self):
        self.driver.find_element(*self.SIDE_NAV_ADD_TO_CART_BTN).click()
        sleep(6)