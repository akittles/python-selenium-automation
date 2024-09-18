from selenium.webdriver.common.by import By

from pages.base_page import Page


class TargetAppPage(Page):
    PP_LINK = (By.XPATH, "//a[text()='Privacy policy']")
    TC_LINK = (By.XPATH, "//a[text()='Target terms and conditions']")

    def open_target_app(self):
        self.open_url('https://www.target.com/c/target-app/')

    def click_pp_link(self):
        # self.click(self.PP_LINK)
        self.wait_and_click(*self.PP_LINK) # had to use wait for test to pass

    def click_tc_link(self):
        self.wait_and_click(*self.TC_LINK)