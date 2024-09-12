from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class SearchResultsPage(Page):
    SEARCH_RESULTS_TXT = (By.XPATH, "//div[@data-test='resultsHeading']")

    def verify_text(self):
        actual_text = self.driver.find_element(*self.SEARCH_RESULTS_TXT).text
        # assert product in actual_text, f'Expected {product} not in actual {actual_text}'
        assert 'coffee' in actual_text, f'Expected coffee not in actual {actual_text}'

    def verify_url(self):
        url = self.driver.current_url
        assert 'coffee' in url, f'Expected "coffee" not in {url}'

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
