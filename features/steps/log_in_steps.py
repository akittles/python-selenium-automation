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


@when('User inputs valid email address and password')
def user_inputs_valid_email_and_password(context):
    context.app.login_page.user_inputs_valid_email_and_password()


@when('User inputs invalid email')
def user_inputs_invalid_email(context):
    context.app.login_page.user_inputs_invalid_email()


@when('User inputs invalid password')
def user_inputs_invalid_password(context):
    context.app.login_page.user_inputs_invalid_password()
    sleep(2)


@when('Click on sign in with password')
def sign_in_with_password(context):
    context.app.login_page.sign_in_with_password()


@then('Verify user is logged in')
def verify_user_is_logged_in(context):
    context.app.login_page.verify_user_is_logged_in()


@then('Verify user on sign_in page')
def verify_sign_in_page(context):
    context.app.login_page.verify_sign_in_page()


@then('Verify user sees Please enter a valid email or phone number')
def verify_invalid_email_or_phone_number(context):
    context.app.login_page.verify_invalid_email_or_phone_number()

# --------SEE NOTE IN LOGIN_PAGE
# @then('Verify user sees Please enter a valid password')
# def verify_invalid_password(context):
#     context.app.login_page.verify_invalid_password()