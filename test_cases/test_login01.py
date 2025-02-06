from tkinter import Scale

from test_cases.baseclass import BaseClass
# from uihelper.helper_file import UI_Helper


class Test_Login(BaseClass):

    #verify valid login
    def test_01_login_with_valid_creds(self):
        self.login.do_login("piyush.alphabin@gmail.com", "Piyush@123")
        self.uihelp.assertion(self.login.get_text(self.login.VERIFY_AFTER_LOGIN_XPATH), "Hi! Reader")

    def test_02_valid_username_invalid_password(self):
        self.login.do_login("piyush.alphabin@gmail.com", "Piyush@12")
        self.uihelp.assertion(self.login.get_text(self.login.INVALID_MSG_AFTER_ENTER_WRONG_CREDS_CSS),
                              "Entered email or password is incorrect")

    


