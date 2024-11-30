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

# open the url
driver.get('https://www.amazon.com/')

# find by ID

driver.find_element(By.ID,'twotabsearchtextbox')
driver.find_element(By.ID,'nav-logo-sprites')

# find by XPATH
driver.find_element(By.XPATH, "//input[@aria-label='Search Amazon']")
driver.find_element(By.XPATH, "//input[@placeholder='Search Amazon']")

# use * to find by attribute only (placeholder is the attribute
driver.find_element(By.XPATH, "//*[@placeholder='Search Amazon']")

# find by multiple attributes
driver.find_element(By.XPATH, "//input[@tabindex='0' and @type= 'text' and @dir='auto']")
driver.find_element(By.XPATH, "//input[@tabindex='0' and @type= 'text']")

driver.find_element(By.ID,'searchDropdownBox') #driver.find_element(By.XPATH, 'searchDropdownBox')


# XPATH by text() function
driver.find_element(By.XPATH, "//a[text()='Best Sellers']")

# text() and attributes
driver.find_element(By.XPATH, "//a[text()='Best Sellers' and @class= 'nav-a  ']")
driver.find_element(By.XPATH, "//a[@class= 'nav-a ' and text()='Best Sellers']")

# connecting to parent node
driver.find_element(By.XPATH, "//div[@id='nav-xshop']//a[text()='Best Sellers']")
driver.find_element(By.XPATH, "//div[@id='nav-xshop']//a[contains(text()='Best')]")
#                                       ^                   ^-----this is selecting the parent nodes
# contains()
driver.find_element(By.XPATH, "//h2[contains(text(), 'under $30')]")