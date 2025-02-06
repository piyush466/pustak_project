import time

from selenium.webdriver.common.by import By

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
        time.sleep(3)

