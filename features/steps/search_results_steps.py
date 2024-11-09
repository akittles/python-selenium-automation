from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import when, then
from time import sleep

ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] a h4")
SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCartButton']")
LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
PRODUCT_IMG = (By.CSS_SELECTOR, 'img')

# SEPARATE THE VARIABLE ABOVE AND PASSING IT IN THE CODE WITH AN * WHEN YOU START GETTING A LOT OF STEPS
# BECAUSE SOME OF THE STEPS MAY REUSE THE SAME LOCATOR. SO ADD THEM TO THE TOP OF THE FILE


@when('Click on Add to Cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()  # find_element always clicks on 1st add to cart btn
# context.driver.find_elements(By.CSS_SELECTOR, "[id*='addToCartButton']")[0].click #find_elements looks for multiples
    context.driver.wait.until(EC.visibility_of_element_located(SIDE_NAV_PRODUCT_NAME))


@when('Store product name')
def store_product_name(context):
    context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
    print(f'Product stored: {context.product_name}')


@when('Confirm Add to Cart button from side navigation')
def side_nav_click_add_to_cart(context):
    context.app.main_page.side_nav_click_add_to_cart()
    # context.driver.find_element(*SIDE_NAV_ADD_TO_CART_BTN).click()
    # sleep(6)
    # can use explicit wait below instead of sleep
    # context.driver.wait.until(EC.visibility_of_element_located(SIDE_NAV_PRODUCT_NAME))


@when('Hover favorites icon')
def hover_fav_icon(context):
    context.app.search_results_page.hover_fav_icon()


@then('Favorites tooltip is shown')
def verify_fav_tooltip(context):
    context.app.search_results_page.verify_fav_tooltip()


@then('Verify search results show for {product}')
def verify_search_results(context, product):
    context.app.search_results_page.verify_search_results(product)


@then('Verify correct search results url opens for {product}')
def verify_url(context, product):
    context.app.search_results_page.verify_product_in_url(product)


@then('Verify that every product has a name and an image')
def verify_products_name_img(context):
    context.app.search_results_page.verify_products_name_img()


