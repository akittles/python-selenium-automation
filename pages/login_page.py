from selenium.webdriver.common.by import By

from pages.base_page import Page


class LoginPage(Page):
    SIGN_IN_MSG = (By.CSS_SELECTOR, "h1[class='sc-fe064f5c-0 sc-315b8ab9-2 WObnm gClYfs']")
    SIGN_IN_PASS_BTN = (By.CSS_SELECTOR, "[id='login']")
    USERNAME_ERROR_MSG = (By.CSS_SELECTOR, "[id='username--ErrorMessage']")
    PASSWORD_ERROR_MSG = (By.CSS_SELECTOR, "[id='password--ErrorMessage']")

    def verify_sign_in_page(self):
        expected_text = 'Sign into your Target account'
        actual_element = self.driver.find_element(*self.SIGN_IN_MSG)
        actual_text = actual_element.text
        print(actual_text)
        assert expected_text in actual_text, f'Expected text {expected_text} is not in actual text {actual_text}'
        print('Test case passed')

    def user_inputs_valid_email_and_password(self):
        username = self.driver.find_element(By.ID, "username").send_keys('<EMAIL>')
        password = self.driver.find_element(By.ID, "password").send_keys('<PASSWORD>')

    def sign_in_with_password(self):
        self.driver.find_element(*self.SIGN_IN_PASS_BTN).click()

    def verify_user_is_logged_in(self):
        self.verify_partial_url('ecom-web')
        # actual_url = self.driver.current_url
        # assert expected_partial_url in actual_url, f'Expected {expected_partial_url} not in {actual_url}'

    def user_inputs_invalid_email(self):
        username = self.driver.find_element(By.ID, "username").send_keys('fda3215654')
        # password = self.driver.find_element(By.ID, "password").send_keys('<PASSWORD>')

    def user_inputs_invalid_password(self):
        # username = self.driver.find_element(By.ID, "username").send_keys('<EMAIL>')
        password = self.driver.find_element(By.ID, "password").send_keys('rtw3t548')

    def verify_invalid_email_or_phone_number(self):
        expected_text = 'Please enter a valid email or phone number'
        actual_element = self.driver.find_element(*self.USERNAME_ERROR_MSG)
        actual_text = actual_element.text
        print(actual_text)
        assert expected_text in actual_text, f'Expected text {expected_text} is not in actual text {actual_text}'
        print('Test case passed')

    #  -----------BELOW METHOD WILL NOT WORK IN AUTOMATED TEST.
    #  -----------STEP WORKS BUT WEBSITE DURING TEST WILL NOT WORK LIKE USER
    #  -----------PASSWORD ERROR MESSAGE WILL NOT SHOW DURING TEST BUT WILL MANUALLY

    # def verify_invalid_password(self):
    #     expected_text = 'Please enter a valid password'
    #     actual_element = self.driver.find_element(*self.PASSWORD_ERROR_MSG)
    #     actual_text = actual_element.text
    #     print(actual_text)
    #     assert expected_text in actual_text, f'Expected text {expected_text} is not in actual text {actual_text}'
    #     print('Test case passed')
