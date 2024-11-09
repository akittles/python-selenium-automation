from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@given('Open reelly main page')
def open_reelly_main_page(context):
    context.driver.get('https://reelly.io/')


@given('Open reelly sign-in page')
def open_reelly_sign_in_page(context):
    context.driver.get('https://soft.reelly.io/sign-in')


@when('Click on open in browser button')
def open_in_browser_button(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href*='sign-in']").click()


@then('Verify signin page UI')
def verify_reelly_signin_page(context):
    context.app.find_element(By.CSS_SELECTOR, "div.html-logo.w-embed").text #Reelly logo
    context.driver.find_element(By.CSS_SELECTOR, ".form-container").text #Sign in or create new account
    context.driver.find_element(By.CSS_SELECTOR, "a[href*='request-password-reset']").text #forgot password
    context.driver.find_element(By.CSS_SELECTOR, "div.sing-in-text").text #create account
    context.driver.find_element(By.CSS_SELECTOR, "#email-2").text #email

    # expected_texted = 'Sign in or create new account'
    # actual_text = context.driver.find_element(By.CSS_SELECTOR, ".form-container").text
    # assert expected_texted in actual_text, f'Expected {expected_texted} not in {actual_text}'


@then('Verify user on signin page')
def verify_url(context):
    url = context.driver.current_url
    assert url == 'https://soft.reelly.io/sign-in'

