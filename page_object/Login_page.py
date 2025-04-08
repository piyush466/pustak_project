import time

from selenium.webdriver.common.by import By
import requests
from uihelper.helper_file import UI_Helper


class Login(UI_Helper):
    #Login
    LOGIN_BTN_CSS = (By.CSS_SELECTOR, "button[class='undefined icon']")
    ENTER_USERNAME_CSS = (By.CSS_SELECTOR, "input.MuiInputBase-input")
    CLICK_ON_PROCEED_XPATH = (By.XPATH, "(//button[@type='submit'])[3]")
    ENTER_PASSWORD_XPATH = (By.XPATH, "//input[@type='password']")
    CLICK_LOGIN_BTN_CSS = (By.CSS_SELECTOR, "button.WLoginNavbar_loginButton__M7mhW")
    VERIFY_AFTER_LOGIN_XPATH = (By.XPATH, "//span[text()='Hi! Reader']")
    INVALID_MSG_AFTER_ENTER_WRONG_CREDS_CSS = (By.CSS_SELECTOR, "#notistack-snackbar")
    IF_USER_ENTER_WRONG_EMAIL_XPATH = (By.XPATH, "//p[text()='Enter valid email']")

    def __init__(self,driver):
        self.driver = driver


    def do_login(self, username, password):
        time.sleep(2)
        self.do_click(self.LOGIN_BTN_CSS)
        self.send_key(self.ENTER_USERNAME_CSS,username)
        self.do_click(self.CLICK_ON_PROCEED_XPATH)
        self.send_key(self.ENTER_PASSWORD_XPATH, password)
        self.do_click(self.CLICK_LOGIN_BTN_CSS)
        self.driver.refresh()
        time.sleep(3)

    def check_broken_links(self):
        self.links = self.driver.find_elements(By.TAG_NAME, "a")

        self.valid_links = []
        self.all_links = []
        self.broken_links = []

        for link in self.links:
            url = link.get_attribute("href")
            self.all_links.append(url)
            if url:
                try:
                    response = requests.get(url)
                    if response.status_code >= 400:
                        self.broken_links.append(url)
                        print(f"this url is broken {url} and the status code is {response.status_code}")
                    else:
                        self.valid_links.append(url)
                        print(f"this is valid url {url} and the status code is {response.status_code}")
                except Exception as E:
                    print(E)





