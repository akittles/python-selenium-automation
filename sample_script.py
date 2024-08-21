from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.implicitly_wait(5)
driver.wait = WebDriverWait(driver, 15)

# open the url
driver.get('https://www.google.com/')

# populate search field
search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('car')


# click search button
# driver.wait.until(EC.element_to_be_clickable((By.NAME, 'btnK')))
# driver.find_element(By.NAME, 'btnK').click()
#-------ABOVE CODE, TECHNICALLY BELOW, YOU CAN DO JUST THIS AND IT WILL FIND ELEMENT
# driver.wait.until(EC.element_to_be_clickable((By.NAME, 'btnK'))).click()
# ----------------------------------------OR---------
# ----------------------------------------------------must add extra ) here for it function
# button = driver.wait.until(EC.element_to_be_clickable((By.NAME, 'btnK')))
# button.click()
# -------------------if you want to seperate this code, if you have a different locator
# --------------------PASS "SEARCH_BTN" INTO THIS FUNCTION

SEARCH_BTN = (By.NAME, 'btnK')
button = driver.wait.until(EC.element_to_be_clickable(SEARCH_BTN))
#if you want to set multiple conditions to be met, place on seperate line
# driver.wait.until(EC.new_window_is_opened())
button.click()

# verify search results
assert 'table' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

driver.quit()
