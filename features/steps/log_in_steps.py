from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

# ------------CHANGE FILE NAME TO LOGIN STEPS------------
@then('Verify user on sign_in page')
def verify_sign_in_page(context):
    context.app.sign_in_menu_page.verify_sign_in_page()

# ---------------------------------------------------------------------
# ------POSSIBLY DELETE BELOW

#--------THE 2 WHENS HERE ARE IN MAIN PAGE STEPS
# @when('Click on sign in')
# def first_signin_btn(context):
#     context.app.header.click_sign_in()
#
# #
# @when('Click on window sign in')
# def window_signin_btn(context):
#     context.app.header.click_window_sign_in()
#     sleep(6)

# -------------THIS STEP IS IN CART STEPS
# @then('Verify your cart is empty message is shown')
# def verify_cart_is_empty(context):
#     expected_text = 'Your cart is empty'
#     actual_element = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")
#     actual_text = actual_element.text
#     print(actual_text)
#     assert expected_text in actual_text, f'Expected text {expected_text} is not in actual text {actual_text}'
#     #
#     print('Test case passed')