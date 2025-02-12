import time
from tkinter import Scale

from selenium.webdriver.common.by import By

from uihelper.helper_file import UI_Helper


class Checkout_Page(UI_Helper):

    CLICK_ON_CHECKOUT_BUTTON_XPATH = (By.XPATH, "//button[text()='Proceed to Checkout ']")
    CLICK_ON_NO_XPATH = (By.XPATH, "(//button[@style='text-transform: capitalize;'])[2]")
    CLICK_ON_DELIVER_HERE_XPATH = (By.XPATH, "//span[text()='Deliver Here']")
    CLICK_ON_PROCEED_TO_PAYMENT_XPATH = (By.XPATH, "//span[text()='Proceed to payment options']")
    RADIO_BUTTON_CASH_DELIVERY_XPATH = (By.XPATH, "(//input[@id='flexRadioDefault2'])[2]")
    CLICK_CONFIRM_ORDER_XPATH = (By.XPATH, "//span[text()='Confirm Order']")
    ORDER_PLACE_MESSAGE_CLASS = (By.XPATH,"//b[@class='jsx-b3e1b6a7c9b96113 OrderThankYou_orderdiv__W9qvK d-flex align-items-center']")

    def __init__(self, driver):
        self.driver = driver

    def goto_checkout(self):
        time.sleep(2)
        self.do_click(self.CLICK_ON_CHECKOUT_BUTTON_XPATH)
        self.do_click(self.CLICK_ON_NO_XPATH)
        self.do_click(self.CLICK_ON_DELIVER_HERE_XPATH)
        self.do_click(self.CLICK_ON_PROCEED_TO_PAYMENT_XPATH)
        self.do_click(self.RADIO_BUTTON_CASH_DELIVERY_XPATH)
        self.do_click(self.CLICK_CONFIRM_ORDER_XPATH)
        self.confirm_text = self.get_text(self.ORDER_PLACE_MESSAGE_CLASS)
        time.sleep(5)


