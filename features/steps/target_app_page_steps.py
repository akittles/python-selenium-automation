from behave import given, when, then
from time import sleep


@given('Open Target App page')
def open_target_app(context):
    context.app.target_app_page.open_target_app()


@given('Store original window')
def store_original_window(context):
    context.original_window = context.app.target_app_page.get_current_window()
    print(context.original_window)


@when('Click on Privacy Policy link')
def click_pp_link(context):
    context.app.target_app_page.click_pp_link()


@when('Switch to new window')
def switch_window(context):
    context.app.target_app_page.switch_to_new_window()


@then('Verify Privacy Policy page opened')
def verify_privacy_policy_opened(context):
    context.app.privacy_page.verify_pp_url()


@then('Close current page')
def close(context):
    pass


@then('Return to original page')
def return_to_original_window(context):
    pass