from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click on sign in')
def click_sign_in_btn(context):
    context.app.header.click_sign_in_btn()


@when('Click on side window sign in')
def side_window_signin_btn(context):
    # context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()
    context.app.main_page.side_window_signin_btn()
    sleep(6)


@when('User inputs email address and password')
def user_inputs_email_and_password(context):
    context.app.login_page.enter_username_password()


@when('Click on sign in with password')
def sign_in_with_password(context):
    context.app.login_page.sign_in_with_password()


@then('Verify user is logged in')
def verify_user_is_logged_in(context):
    context.app.login_page.verify_user_is_logged_in()


@then('Verify user on sign_in page')
def verify_sign_in_page(context):
    context.app.login_page.verify_sign_in_page()


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
