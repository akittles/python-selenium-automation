from selenium.webdriver.common.by import By


from pages.base_page import Page
from time import sleep


class ChooseOptionsMenuPage(Page):
    SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCartButton']")

    def side_nav_click_add_to_cart(self):
        self.driver.find_element(*self.SIDE_NAV_ADD_TO_CART_BTN).click()
        sleep(6)
