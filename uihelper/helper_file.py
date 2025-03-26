import logging
from selenium import webdriver
from selenium.webdriver.common.by import ByType
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.logger import setup_logger
import datetime

class UI_Helper:

    def __init__(self,driver):
        self.driver = driver

        # self.wait = WebDriverWait(self.driver,20)

    def do_click(self,by_locator):
        WebDriverWait(self.driver,20).until(EC.presence_of_element_located(by_locator)).click()

    def send_key(self,by_locator,text):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(by_locator)).send_keys(text)

    def get_title(self):
        return self.driver.title

    def drop_down(self,by_locator,value):
        self.element = self.wait.until(EC.presence_of_element_located(by_locator))
        self.select = Select(self.element)
        self.select.select_by_value(value)

    def get_text(self,by_locator):
        return  WebDriverWait(self.driver,20).until(EC.presence_of_element_located(by_locator)).text

    def assertion(self,actual_result, expected_result):
        assert actual_result == expected_result, "The result is not match"

    def switch_to_window(self):
        self.windows = self.driver.window_handles
        self.driver.switch_to.window(self.windows[1])

    def take_screenshot(self):
        now = datetime.datetime.now()
        current_time = now.strftime("%d_%m_%Y_%H_%M_%S")
        name = f"Screenshot_{current_time}"
        file_path = f"C:\\Users\\Piyush Dravyakar\\Pustak_project\\pythonProject\\screenshots\\{name}.png"
        self.driver.save_screenshot(file_path)
