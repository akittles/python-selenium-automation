import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

from app.application import Application
from support.logger import logger


def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """

    driver_path = 'C:/Users/Owner/python-selenium-automation/chromedriver-win64/chromedriver.exe'
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)
    context.driver = webdriver.Chrome()

    # --------MOBILE WEB TESTING-------------

    # from selenium.webdriver.chrome.options import Options
    # mobile_emulation = {
    #     "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
    #     "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19",
    #     "clientHints": {"platform": "Android", "mobile": True}}
    # chrome_options = Options() #chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    # driver = webdriver.Chrome(chrome_options=chrome_options) # driver = webdriver.Remote(appium_server_url, options=capabilities_options)

    # mobile_emulation = {"deviceName": "Nexus 5"}
    # options = webdriver.ChromeOptions()
    # options.add_experimental_option("mobileEmulation", mobile_emulation)
    # driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub', options=options)
    # context.driver = driver

    #
    # mobile_emulation = {"deviceName": "Nexus 5"}
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    # driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub',
    #                           desired_capabilities=chrome_options.to_capabilities())


    # ----------------HEADLESS FIREFOX--------------------------------------

    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Firefox(service=service)

    # context.driver = webdriver.Safari() #CAN ONLY RUN ON MAC OR IOS

    # ---------------------------------------------------------------

    ### HEADLESS MODE #### TESTING CHROME IN THE TERMINAL
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )

    # Command to run tests with Allure & Behave:
    # behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/target_search.feature

    # -----WHEN RUNNING TESTS FROM THE TERMINAL USE COMMAND LINE
    #           behave -f allure_behave.formatter:AllureFormatter -o %/allure_result_folder%./feature

    # ----NOTE----------Run all pages
    # --EXAMPLE: behave -f allure_behave.formatter:AllureFormatter -o test_results/features/tests/page.feature

    # ---NOTE---put a space after test_result/ to only test a specific feature
    # ---------------Run a certain feature                          # test_results/ features/tests/settings.feature

    # behave -f allure_behave.formatter:AllureFormatter -o      %allure_result_folder%.    /features

    # -------------------------------------------------------------------

    ### BROWSERSTACK ###
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    # bs_user = 'anthonykittles_DMlABu'
    # bs_key = 'UUbrpL7fPHuFFe9Y7zo4'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    # options = Options()
    # bstack_options = {
    #     "os": "Windows",
    #     "osVersion": "11",
    #     'browserName': 'chrome',
    #     'sessionName': scenario_name
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)

    ### BROWSERS WITH DRIVERS: provide path to the driver file ###--old way of doing things,
    #           #Not needed but may fix later
    # service = Service(executable_path='/Users/Owner/python-selenium-automation/geckodriver')
    # context.driver = webdriver.Firefox(service=service)

    ######## NORMAL FUNCTIONS ############
    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 15) # aka explicit wait

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    logger.info(f'\nStarted scenario: {scenario.name}')
    browser_init(context, scenario.name)


def before_step(context, step):
    logger.info(f'\nStarted step: {step.name}')
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        logger.error(f'\nStep failed: {step}')
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
