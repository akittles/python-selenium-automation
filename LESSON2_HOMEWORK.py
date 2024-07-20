from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()


# ----------Part 1
# open the url
# driver.get('https://www.amazon.com/')
#
# driver.find_element(By.XPATH, "//i[@aria-label='Amazon']")
# driver.find_element(By.ID, 'ap_email')
# driver.find_element(By.ID, 'continue')
# driver.find_element(By.XPATH, "//a[text()='Conditions of Use']")
# driver.find_element(By.XPATH, "//a[text()='Privacy Notice']")
# driver.find_element(By.XPATH, "//*[@class='a-row a-expander-container a-expander-inline-container']")
# driver.find_element(By.ID, 'auth-fpp-link-bottom')
# driver.find_element(By.ID, 'ap-other-signin-issues-link')
# driver.find_element(By.ID, 'ap-other-signin-issues-link')
# driver.find_element(By.ID, 'createAccountSubmit')


# ----------Part 2

# driver.get('https://www.target.com/')
# driver.find_element(By.XPATH, "//a[@aria-label='Account, sign in']").click()
# driver.find_element(By.XPATH, "//div[@data-test='content-wrapper']").click()
#
# sleep(5)# inserted here because another page tries to open first then goes to sign in page
# driver.find_element(By.XPATH, "//*[text()='Sign into your Target account']")
# driver.find_element(By.XPATH, "//button[@id='login']")
#
# sleep(10)
#
# # verify
# expected_result = "Sign into your Target account" and driver.find_element(By.XPATH, "//button[@id='login']")
#
# actual_result = driver.find_element(By.XPATH, "//*[text()='Sign into your Target account']").text and driver.find_element(By.XPATH, "//button[@id='login']")
#
#
#
# print(actual_result)
# print('Test passed')


# Bonus test case

driver.get('https://www.target.com/')
driver.find_element(By.XPATH, "//input[@aria-label='What can we help you find? suggestions appear below']").send_keys('milk')
driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()

sleep(6)

expected_result = 'milk'
actual_result = driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
print(actual_result)

assert expected_result in actual_result, f'Expected {expected_result}, is not in actual text {actual_result}'

print('Test passed')
driver.quit()

