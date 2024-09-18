from behave import given, when, then
from time import sleep


@given('Open Target App page')
def open_target_app(context):
    context.app.target_app_page.open_target_app()


@given('Store original window')
def store_original_window(context):
    context.original_window = context.app.target_app_page.get_current_window()


@when('Click on Privacy Policy link')
def click_pp_link(context):
    context.app.target_app_page.click_pp_link()


@when('Click on Target terms and conditions link')
def click_tc_link(context):
    context.app.target_app_page.click_tc_link()


@when('Switch to the newly opened window')
def switch_to_newly_opened_window(context):
    context.app.target_app_page.switch_to_newly_opened_window()


@when('Switch to new window')
def switch_window(context):
    context.app.target_app_page.switch_to_new_window()


@then('Verify Privacy Policy page opened')
def verify_privacy_policy_opened(context):
    context.app.privacy_page.verify_pp_url()


@then('Verify Terms and Conditions page is opened')
def verify_terms_and_conditions_opened(context):
    context.app.terms_conditions_page.verify_tc_url()


@then('Close current page')
def close(context):
    context.app.privacy_page.close()


@then('Return to original page')
def return_to_original_window(context):
    context.app.privacy_page.switch_to_window_by_id(context.original_window)


@then('User can close new window and switch back to original')
def close_new_window_and_switch_back_to_original(context):
    context.app.terms_conditions_page.switch_to_window_by_id(context.original_window)