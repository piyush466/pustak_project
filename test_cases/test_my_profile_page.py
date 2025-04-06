from selenium.webdriver.common.devtools.v128.emulation import SensorReading

from test_cases import test_login01
from test_cases.baseclass import BaseClass


class Test_MyProfile(BaseClass):

    def test_01_navigate_my_profile_page(self):
        self.login.do_login(test_login01.username,test_login01.password)
        self.my_profile.navigate_my_profile()
        self.uihelp.assertion(self.my_profile.my_profile_page_text, "Enter your personal details")

    def test_02_user_can_update_fname_and_lname(self):
        self.login.do_login(test_login01.username, test_login01.password)
        self.my_profile.navigate_my_profile()
        self.my_profile.remove_text_from_textbox()
        self.my_profile.enter_fname_and_lname("Piyush", "Dr12")
        self.uihelp.assertion(self.my_profile.verify_success_message, "Profile Updated Successfully")

    def test_03_user_can_navigate_to_manage_address_page(self):
        self.login.do_login(test_login01.username, test_login01.password)
        self.my_profile.navigate_my_profile()
        self.my_profile.navigate_manage_address()
        self.uihelp.assertion(self.my_profile.verify_manage_address, "Manage Address")

    def test_04_user_can_add_new_address(self):
        self.login.do_login(test_login01.username, test_login01.password)
        self.my_profile.navigate_my_profile()
        self.my_profile.navigate_manage_address()
        self.my_profile.add_new_address("piyush", 444607, "amravati", "hotel",8411878794, 8411878794)
        self.uihelp.assertion(self.my_profile.verify_succes_message_address, "Address Added Successfully")

    def test_05_user_can_delete_address(self):
        self.login.do_login(test_login01.username, test_login01.password)
        self.my_profile.navigate_my_profile()
        self.my_profile.navigate_manage_address()
        self.my_profile.add_new_address("piyush", 444607, "amravati", "hotel", 8411878794, 8411878794)
        self.my_profile.delete_address()
        self.uihelp.assertion(self.my_profile.verify_delete_success_message, "Address deleted succesfully")

    def test_06_user_can_edit_the_address(self):
        self.login.do_login(test_login01.username, test_login01.password)
        self.my_profile.navigate_my_profile()
        self.my_profile.navigate_manage_address()
        self.my_profile.add_new_address("piyush", 444607, "amravati", "hotel", 8411878794, 8411878794)
        self.my_profile.edit_address("Akash")
        self.uihelp.assertion(self.my_profile.verify_edit_success_message, "Address Edited Successfully")

    def test_07(self):
        self.uihelp.take_screenshot()













