# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from time import sleep
#
# # get the path to the ChromeDriver executable
# driver_path = ChromeDriverManager().install()
#
# # create a new Chrome browser instance
# service = Service(driver_path)
# driver = webdriver.Chrome(service=service)
# driver.maximize_window()
#
# # open the url
# driver.get('https://www.amazon.com/')
#
# # find by CSS, using ID: use # for id
# #  tag#id
# # This is the same as driver.find_element(By.ID, "twotabsearchtextbox")
# driver.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox")
# driver.find_element(By.CSS_SELECTOR, "input#twotabsearchtextbox")
# # -------------------------------------------tag---id
#
# # Find by css, using classes: .classname
# driver.find_element(By.CSS_SELECTOR, ".nav-input")
# driver.find_element(By.CSS_SELECTOR, ".nav-input.nav-progressive-attribute")
# # multiple classes---------------------------class--------class
#
# # tag + classes
# # tag.class
# driver.find_element(By.CSS_SELECTOR, "input.nav-input.nav-progressive-attribute")
# # -------------------------------------tag---class----class
#
# # tag + ID + classes
# driver.find_element(By.CSS_SELECTOR, "input#twotabsearchtextbox.nav-input.nav-progressive")
#
# # attributes
# driver.find_element(By.CSS_SELECTOR, "[placeholder='Search Amazon']")
# driver.find_element(By.CSS_SELECTOR, "[placeholder='Search Amazon'][type='text']")
#
# # tag + attributes
# driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search Amazon'][type='text']")
#
# # tag + #id + .class + [attributes] #order doesn't matter but is recommended
# driver.find_element(By.CSS_SELECTOR, "input#twotabsearchtextbox.nav-input[placeholder='Search Amazon'][type='text']")
#
# # -------------------------------------tag-----#id----------------class-----------attribute-------------attribute
#
#
# # attributes, partial match
# driver.find_element(By.CSS_SELECTOR, "[placeholder*='Search Ama']") #Ama = Amazon
# driver.find_element(By.CSS_SELECTOR, "a[href*='ap_signin_notification_privacy_notice?']")
# driver.find_element(By.CSS_SELECTOR, "a[class*='ap_signin_notification_privacy_notice?']")
# -------------------------------------tag--attribute

#
# # Multiple nodes. parent to child # separate nodes with a space in between
# driver.find_element(By.CSS_SELECTOR, "div.a-box div#legalTextRow a[href*='condition']")
# # --------------------------------------------parent-----child-----------attribute