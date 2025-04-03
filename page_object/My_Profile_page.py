import time

from uihelper.helper_file import UI_Helper
from selenium.webdriver.common.by import By

class My_Profile(UI_Helper):

    CLICK_ON_HI_READER_ID = (By.ID, "loginBtn")
    CLICK_ON_MY_PROFILE_XPATH = (By.XPATH, "//*[text()=' My Profile']")
    NAVIGATE_PAGE_TEXT_CSS = (By.CSS_SELECTOR, "[class*='Myprofile_inputTitle']")

    def __init__(self, driver):
        self.driver = driver

    def navigate_my_profile(self):
        self.do_click(self.CLICK_ON_HI_READER_ID)
        self.do_click(self.CLICK_ON_MY_PROFILE_XPATH)
        self.my_profile_page_text =self.get_text(self.NAVIGATE_PAGE_TEXT_CSS)
        print(self.my_profile_page_text)
        # time.sleep(4)