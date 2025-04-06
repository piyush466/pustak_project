import time

import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from page_object.My_Profile_page import My_Profile
from page_object.Product_Page import Product_Page
from page_object.locators import Locators
from uihelper.helper_file import UI_Helper
from selenium.webdriver.support import expected_conditions as EC

class WishListPage(UI_Helper,Locators):

    def wishlist_product_add(self):
        self.do_click(self.ADD_PRODUCT_IN_WISHLIST_XPATH)
        time.sleep(2)
        self.do_click(self.CLICK_ON_VIEW_WSIHLIST)
        time.sleep(5)
        self.text_show = self.text_displayed(self.CAPTURE_TEXT_FORM_WISHLIST)
        self.do_click(self.REMOVE_THE_WISHLIST_PRODUCT_XPATH)
        time.sleep(5)


    def remove_product_from_wishlist(self):
        self.do_click(self.ADD_PRODUCT_IN_WISHLIST_XPATH)
        self.do_click(self.CLICK_ON_VIEW_WSIHLIST)
        self.do_click(self.REMOVE_THE_WISHLIST_PRODUCT_XPATH)
        self.verify_remove_message = self.get_text(self.VERIFY_REMOVE_MESSAGE_XPATH)
        print(self.verify_remove_message)






