from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.logger import setup_logger
import datetime

class UI_Helper:

    logs = setup_logger()

    def __init__(self, driver):
        self.driver = driver

    def take_screenshot(self):
        now = datetime.datetime.now()
        current_time = now.strftime("%d_%m_%Y_%H_%M_%S")
        name = f"Screenshot_{current_time}"
        file_path = f"C:\\Users\\Piyush Dravyakar\\pythonProject_pustak\\screenshots\\{name}.png"
        self.driver.save_screenshot(file_path)
        self.logs.error(f"Screenshot taken: {file_path}")

    def do_click(self, by_locator):
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(by_locator)).click()
            self.logs.info(f"Clicked element located by: {by_locator}")
        except Exception as E:
            self.logs.error(f"Exception occurred while doing click: {E}")
            self.take_screenshot()

    def send_key(self, by_locator, text):
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(by_locator)).send_keys(text)
            self.logs.info(f"Sent keys '{text}' to element located by: {by_locator}")
        except Exception as E:
            self.logs.error(f"Exception occurred while sending text: {E}")
            self.take_screenshot()

    def get_title(self):
        try:
            title = self.driver.title
            self.logs.info(f"Page title retrieved: {title}")
            return title
        except Exception as E:
            self.logs.error(f"Exception occurred while getting title: {E}")
            self.take_screenshot()

    def drop_down(self, by_locator, value):
        try:
            element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(by_locator))
            select = Select(element)
            select.select_by_value(value)
            self.logs.info(f"Selected value '{value}' from dropdown located by: {by_locator}")
        except Exception as E:
            self.logs.error(f"Exception occurred while selecting value from drop down: {E}")
            self.take_screenshot()

    def get_text(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))
            text = element.text
            self.logs.info(f"Text retrieved from element located by {by_locator}: {text}")
            return text
        except Exception as e:
            self.logs.error(f"Exception occurred while getting text: {e}")
            self.take_screenshot()

    def assertion(self, actual_result, expected_result):
        try:
            assert actual_result == expected_result, "The result does not match"
            self.logs.info(f"Assertion passed: Actual = {actual_result}, Expected = {expected_result}")
        except Exception as E:
            self.logs.error(f"Exception occurred while matching the data: {E}")
            self.take_screenshot()


    def switch_to_window(self):
        try:
            windows = self.driver.window_handles
            self.driver.switch_to.window(windows[1])
            self.logs.info("Switched to new window successfully.")
        except Exception as E:
            self.logs.error(f"Exception occurred while switching window: {E}")
            self.take_screenshot()

    def clear_text(self, by_locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator)).clear()
            self.logs.info(f"Cleared text of element located by: {by_locator}")
        except Exception as E:
            self.logs.error(f"Exception occurred while clearing")
            self.take_screenshot()

    def text_displayed(self, by_locator):
        try:
            return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).is_displayed()
            self.logs.info(f"Element {by_locator} is displayed")
        except Exception as E:
            self.logs.error(f"Exception occurred while checking if element is displayed: {E}")
            self.take_screenshot()

