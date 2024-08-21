from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify sign in page opens')
def verify_sign_page(context):
    expected_text = 'Sign into your Target account'
    actual_element = context.driver.find_element(By.CSS_SELECTOR, "h1[class='sc-fe064f5c-0 sc-315b8ab9-2 WObnm gClYfs']")
    actual_text = actual_element.text
    print(actual_text)
    assert expected_text in actual_text, f'Expected text {expected_text} is not in actual text {actual_text}'
    #
    print('Test case passed')


# sign in----------------------NOT IN LANAS MAIN PAGE* POSSIBLY DELETE
# @when('Click on sign in')
# def first_signin(context):
#     context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/AccountLink']").click()
#
# @when('Click on window sign in')
# def window_signin(context):
#     context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()
#     sleep(6)


# ---------------------------------------------------------------------
# ------POSSIBLY DELETE BELOW
# @then('Verify your cart is empty message is shown')
# def verify_cart_is_empty(context):
#     expected_text = 'Your cart is empty'
#     actual_element = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")
#     actual_text = actual_element.text
#     print(actual_text)
#     assert expected_text in actual_text, f'Expected text {expected_text} is not in actual text {actual_text}'
#     #
#     print('Test case passed')