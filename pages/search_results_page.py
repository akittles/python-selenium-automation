from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULTS_TXT = (By.XPATH, "//div[@data-test='resultsHeading']")

    FAVORITES_BTN = (By.CSS_SELECTOR, "[data-test='FavoritesButton']")
    FAVORITES_TOOLTIP_TXT = (By.XPATH, "//*[text()='Click to sign in and save']")
    # LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")

    def hover_fav_icon(self):
        # fav_icon = self.find_element(*self.FAVORITES_BTN)
        # actions = ActionChains(self.driver)
        # actions.move_to_element(fav_icon)
        # actions.perform()
        # sleep(2)
        self.wait_for_element_appear(*self.FAVORITES_BTN)
        self.hover_element(*self.FAVORITES_BTN)
        # sleep(4)

    def verify_fav_tooltip(self):
        self.wait_for_element_appear(*self.FAVORITES_TOOLTIP_TXT)

    def verify_search_results(self, expected_product):
        self.verify_partial_text(expected_product, *self.SEARCH_RESULTS_TXT)

    def verify_product_in_url(self, expected_product):
        self.verify_partial_url(expected_product)

    def verify_products_name_img(self):
        product_title = (By.CSS_SELECTOR, "[data-test='product-title']")
        product_img = (By.CSS_SELECTOR, 'img')

        self.driver.execute_script("window.scrollBy(0,2000)", "")
        sleep(4)
        self.driver.execute_script("window.scrollBy(0,2000)", "")
        all_products = self.driver.find_elements(By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")  # [WebEl1, WebEl2, WebEl3, WebEl4]
        for product in all_products:
            title = product.find_element(*product_title).text
            assert title, 'Product title not shown'
            print(title)
            product.find_element(*product_img)


from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULTS_TXT = (By.XPATH, "//div[@data-test='resultsHeading']")

    FAVORITES_BTN = (By.CSS_SELECTOR, "[data-test='FavoritesButton']")
    FAVORITES_TOOLTIP_TXT = (By.XPATH, "//*[text()='Click to sign in and save']")

    def hover_fav_icon(self):
        # fav_icon = self.find_element(*self.FAVORITES_BTN)
        # actions = ActionChains(self.driver)
        # actions.move_to_element(fav_icon)
        # actions.perform()
        self.wait_for_element_appear(*self.FAVORITES_BTN)
        self.hover_element(*self.FAVORITES_BTN)

    def verify_fav_tooltip(self):
        self.wait_for_element_appear(*self.FAVORITES_TOOLTIP_TXT)

    def verify_search_results(self, expected_product):
        self.verify_partial_text(expected_product, *self.SEARCH_RESULTS_TXT)

    def verify_product_in_url(self, expected_product):
        self.verify_partial_url(expected_product)