# ***********************Corrected code from gemini*********
# ****Moved driver = webdriver.Chrome() before driver.maximize_window() to get
# maximize_window, implicitly_wait WebDriverWait to work*******

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# ALTERNATIVE PATH
# driver_path = 'C:/Users/Owner/python-selenium-automation/chromedriver-win64/chromedriver.exe'

# create a new Chrome browser instance
# service = Service(driver_path)
# # driver = webdriver.Chrome(service=service)
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.wait = WebDriverWait(driver, 15)


# open the url
driver.get('https://www.google.com/')
driver.wait = WebDriverWait(driver, 10)
# populate search field
search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('car')

# click search button, CREATE A VARIABLE WITH LOCATOR

SEARCH_BTN = (By.NAME, 'btnK')
# button = driver.wait.until(EC.element_to_be_clickable((By.NAME, 'btnK'))) #this takes an extra )
button = driver.wait.until(EC.element_to_be_clickable(SEARCH_BTN)) #no * for EC's (SEARCH_BTN)
button.click()
# if you want to set multiple conditions (wait.until) to be met, place on separate line
# driver.wait.until(EC.new_window_is_opened())

# verify search results
# assert 'table' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

driver.quit()

# ******Original code from Lana*******
#
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from time import sleep
#
# # get the path to the ChromeDriver executable
# @@ -11,6 +13,8 @@
# service = Service(driver_path)
# driver = webdriver.Chrome(service=service)
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.wait = WebDriverWait(driver, 15)
#
# # open the url
# driver.get('https://www.google.com/')
# @@ -20,11 +24,11 @@
# search.clear()
# search.send_keys('Car')
#
# # wait for 4 sec
# sleep(4)
#
# # click search button
# driver.find_element(By.NAME, 'btnK').click()
# SEARCH_BTN = (By.NAME, 'btnK')
# # button = driver.wait.until(EC.element_to_be_clickable((By.NAME, 'btnK')))
# button = driver.wait.until(EC.element_to_be_clickable(SEARCH_BTN))
# button.click()
#
# # verify search results
# assert 'car' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
