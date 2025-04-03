import time

from selenium.webdriver.common.devtools.v128.emulation import SensorReading

from uihelper.helper_file import UI_Helper
from selenium.webdriver.common.by import By

class My_Profile(UI_Helper):

    CLICK_ON_HI_READER_ID = (By.ID, "loginBtn")
    CLICK_ON_MY_PROFILE_XPATH = (By.XPATH, "//*[text()=' My Profile']")
    NAVIGATE_PAGE_TEXT_CSS = (By.CSS_SELECTOR, "[class*='Myprofile_inputTitle']")
    ENTER_FNAME_BY_ID = (By.ID, "first_name")
    ENTER_LNAME_BY_ID = (By.ID, "last_name")
    CLICK_ON_UPDATE_XPATH = (By.XPATH, "//*[text()='Update']")
    VALIDATION_UPDATE_TEXT_XPATH = (By.XPATH, "//*[text()='Profile Updated Successfully']")
    #Manage Address page
    NAVIGATE_TO_MANAGE_ADDRESS_PAGE_XPATH = (By.XPATH, "//*[text()='Manage Address']")
    CLICK_ON_ADD_NEW_ADDRESS_XPATH = (By.XPATH, "(//*[text()=' Add New Address'])[1]")
    VERIFY_MANAGE_ADDRESS_PAGE_XPATH = (By.XPATH, "//b[text()='Manage Address']")
    #add new address
    CLICK_ADD_NEW_ADDRESS_XPATH = (By.XPATH, "(//*[text()=' Add New Address'])[1]")
    ENTER_NAME_BY_NAME = (By.NAME,"fullname")
    ENTER_PINCODE_BY_NAME = (By.NAME, "pincode")
    ENTER_ADDRESS_BY_NAME = (By.NAME, "address1")
    ENTER_LANDMARK_BY_NAME = (By.NAME, "landmark")
    ENTER_PHONE_NO_BY_NAME = (By.NAME, "phone_no")
    ENTER_WP_NO_BY_NAME = (By.NAME, "alt_phone_no")
    CLICK_ON_ADD_ADDRESS_XPATH = (By.XPATH, "//*[text()='Add Address']")
    VERIFY_ADDRESS_ADDEDE_SUCCESFUL_XPATH = (By.XPATH, "//*[text()='Address Added Successfully']")

    def __init__(self, driver):
        self.driver = driver

    def navigate_my_profile(self):
        self.do_click(self.CLICK_ON_HI_READER_ID)
        self.do_click(self.CLICK_ON_MY_PROFILE_XPATH)
        self.my_profile_page_text =self.get_text(self.NAVIGATE_PAGE_TEXT_CSS)

    def enter_fname_and_lname(self,fname,lname):
        self.clear_text(self.ENTER_FNAME_BY_ID)
        self.clear_text(self.ENTER_LNAME_BY_ID)
        self.send_key(self.ENTER_FNAME_BY_ID, fname)
        self.send_key(self.ENTER_LNAME_BY_ID, lname)
        self.do_click(self.CLICK_ON_UPDATE_XPATH)
        self.verify_success_message = self.get_text(self.VALIDATION_UPDATE_TEXT_XPATH)


    def remove_text_from_textbox(self):
        self.clear_text(self.ENTER_FNAME_BY_ID)
        self.clear_text(self.ENTER_LNAME_BY_ID)
        self.do_click(self.CLICK_ON_UPDATE_XPATH)

#Manage Address Page

    def navigate_manage_address(self):
        self.do_click(self.NAVIGATE_TO_MANAGE_ADDRESS_PAGE_XPATH)
        self.verify_manage_address = self.get_text(self.VERIFY_MANAGE_ADDRESS_PAGE_XPATH)

    def add_new_address(self,name,pincode,address,landmark,mobile_no,wp_no):
        self.do_click(self.CLICK_ADD_NEW_ADDRESS_XPATH)
        self.send_key(self.ENTER_NAME_BY_NAME, name)
        self.send_key(self.ENTER_PINCODE_BY_NAME, pincode)
        self.send_key(self.ENTER_ADDRESS_BY_NAME, address)
        self.send_key(self.ENTER_LANDMARK_BY_NAME, landmark)
        self.send_key(self.ENTER_PHONE_NO_BY_NAME,mobile_no)
        self.send_key(self.ENTER_WP_NO_BY_NAME, wp_no)
        self.do_click(self.CLICK_ON_ADD_ADDRESS_XPATH)
        self.verify_succes_message_address = self.get_text(self.VERIFY_ADDRESS_ADDEDE_SUCCESFUL_XPATH)
        time.sleep(5)




