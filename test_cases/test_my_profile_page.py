from test_cases import test_login01
from test_cases.baseclass import BaseClass


class Test_MyProfile(BaseClass):

    def test_01_navigate_my_profile_page(self):
        self.login.do_login(test_login01.username,test_login01.password)
        self.my_profile.navigate_my_profile()
        self.uihelp.assertion(self.my_profile.my_profile_page_text, "Enter your personal details")