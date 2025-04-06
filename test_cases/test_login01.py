from dotenv import load_dotenv

from test_cases.baseclass import BaseClass
from page_object.Login_page import Login
from test_data import Login_creds
import configparser
import os
config = configparser.ConfigParser()
config.read(Login_creds.path_of_config_file)
env_path  = config.get("env path", "env_file_path")
load_dotenv(env_path)
username = os.getenv("USEREMAIL")
password = os.getenv("PASSWORD")

class Test_Login(BaseClass):


    #verify valid login
    def test_01_login_with_valid_creds(self):
        self.login.do_login(username,password)
        self.uihelp.assertion(self.login.get_text(self.login.VERIFY_AFTER_LOGIN_XPATH), "Hi! Reader")

    def test_02_valid_username_invalid_password(self):
        self.login.do_login(username,"password")
        self.uihelp.assertion(self.login.get_text(self.login.INVALID_MSG_AFTER_ENTER_WRONG_CREDS_CSS),
                              "Entered email or password is incorrect")

    def test_02_check_the_broken_links(self):
        self.login.check_broken_links()
        assert len(self.login.broken_links) == 0



    


