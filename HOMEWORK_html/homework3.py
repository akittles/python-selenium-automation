from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
# service = Service(driver_path)
# driver = webdriver.Chrome(service=service)
# driver.maximize_window()
# #
#
# driver.get('https://www.amazon.com/')
# driver.find_element(By.CSS_SELECTOR, "[aria-label='Amazon']")
# driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")
# driver.find_element(By.CSS_SELECTOR, "#ap_customer_name")
# driver.find_element(By.CSS_SELECTOR, "#ap_email")
# driver.find_element(By.CSS_SELECTOR, "#ap_password")
# driver.find_element(By.CSS_SELECTOR, "#ap_password_check")
# driver.find_element(By.CSS_SELECTOR, "#continue")
# driver.find_element(By.CSS_SELECTOR, "a[href*='ref=ap_register_notification_condition_of_use?']")
# driver.find_element(By.CSS_SELECTOR, "a[href*='ref=ap_register_notification_privacy_notice?']")
# driver.find_element(By.CSS_SELECTOR, ".a-link-emphasis")

#
#
#
#
#
# #
# # # find search and enter text
# # driver.find_element(By.ID, 'search').send_keys('tea')
# # # click search
# # driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
# #
# # sleep(6)
# #
# #
# # # verify
# # expected_text = 'tea'
# # actual_text = driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
# # print(actual_text)
# # assert expected_text in actual_text, f'Expected text {expected_text} is not in actual text {actual_text}'
# #
# # print('Test case passed')
# #
# # driver.quit()