from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_target(context):
    context.app.main_page.open()


@when('Search for {product}')
def search_product(context, product):
    print('Step:', product)
    context.app.header.search_product(product)


@when('Click on Cart icon')
def click_cart(context):
    context.app.header.click_cart()

    #-------------DO NOT DO THIS!!---------------
    # # find empty cart (THIS IS AN EXAMPLE OF HAVING 2 OF THE SAME STEPS)
    # @when('Click on cart icon')
    # def click_cart_icon(context):
    #     context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()
    #     sleep(6)
    #     context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")


@then('Verify header in shown')
def verify_header_present(context):
    context.driver.find_element(By.CSS_SELECTOR, "[class*= styles_utilityHeaderContainer]")


@then('Verify header has {number} links')
def verify_header_link_amount(context, number):
    number = int(number) # turns string "6" into integer 6
    links = context.driver.find_elements(By.CSS_SELECTOR, "[id*= 'utilityNav']")
    assert len(links) == number, f'Expected {number} links, but got {len(links)}'
    # context.driver.find_elements(By.CSS_SELECTOR, "[id*='utilityNav2613542']")


@then('Verify can click every link')
def verify_click_links(context):
    links = context.driver.find_elements(By.CSS_SELECTOR, "[id*='utilityNav']")

    for i in range(len(links)):
        # Search for links again because their internal IDs changed:
        # to avoid Stale Element Exception
        links = context.driver.find_elements(By.CSS_SELECTOR, "[id*='utilityNav']")
        print(f'Clicking on link {links[i].text}')
        links[i].click()
        sleep(4)

    # ************************     NOTES        ***************************


    # -----if just trying to count or verify the amount of elements on a page, do this
    # number = int(number)  # turns string "6" into integer 6
    # links = context.driver.find_elements(By.CSS_SELECTOR, "[id*= 'utilityNav']")
    # assert len(links) == number, f'Expected {number} links, but got {len(links)}'

    # -------------------only have this line of code below-------
    # links = context.driver.find_elements(By.CSS_SELECTOR, "[id*= 'utilityNav']")
    # assert len(links) > 0 #ALWAYS USE ASSERT TO VERIFY ELEMENTS ARE THERE WHEN USING find_elementS

