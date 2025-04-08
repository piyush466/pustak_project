from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import setup_logger
import datetime

class UI_Helper:

    logs = setup_logger()

    def __init__(self, driver):
        """
        Constructor to initialize the UI_Helper class with the WebDriver instance.
        """
        self.driver = driver

    def take_screenshot(self):
        """
        Captures a screenshot with the current timestamp and saves it in the 'screenshots' directory.
        Useful for debugging when test steps fail.
        """
        now = datetime.datetime.now()
        current_time = now.strftime("%d_%m_%Y_%H_%M_%S")
        name = f"Screenshot_{current_time}"
        file_path = f"C:\\Users\\Piyush Dravyakar\\pythonProject_pustak\\screenshots\\{name}.png"
        self.driver.save_screenshot(file_path)
        self.logs.error(f"Screenshot taken: {file_path}")

    def do_click(self, by_locator):
        """
        Clicks on a web element identified by the given locator.
        Waits until the element is present before clicking.
        """
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(by_locator)).click()
            self.logs.info(f"Clicked element located by: {by_locator}")
        except Exception as E:
            self.logs.error(f"Exception occurred while doing click: {E}")
            self.take_screenshot()

    def send_key(self, by_locator, text):
        """
        Sends text to an input field identified by the given locator.
        Waits until the element is present before sending text.
        """
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(by_locator)).send_keys(text)
            self.logs.info(f"Sent keys '{text}' to element located by: {by_locator}")
        except Exception as E:
            self.logs.error(f"Exception occurred while sending text: {E}")
            self.take_screenshot()

    def get_title(self):
        """
        Returns the current page title.
        Useful for validating the navigation or current page context.
        """
        try:
            title = self.driver.title
            self.logs.info(f"Page title retrieved: {title}")
            return title
        except Exception as E:
            self.logs.error(f"Exception occurred while getting title: {E}")
            self.take_screenshot()

    def drop_down(self, by_locator, value):
        """
        Selects a value from a dropdown element using 'select_by_value'.
        Waits until the element is present before selecting.
        """
        try:
            element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(by_locator))
            select = Select(element)
            select.select_by_value(value)
            self.logs.info(f"Selected value '{value}' from dropdown located by: {by_locator}")
        except Exception as E:
            self.logs.error(f"Exception occurred while selecting value from drop down: {E}")
            self.take_screenshot()

    def get_text(self, by_locator):
        """
        Retrieves and returns the visible text of an element.
        Waits until the element is present before accessing the text.
        """
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator))
            text = element.text
            self.logs.info(f"Text retrieved from element located by {by_locator}: {text}")
            return text
        except Exception as e:
            self.logs.error(f"Exception occurred while getting text: {e}")
            self.take_screenshot()

    def assertion(self, actual_result, expected_result):
        """
        Asserts that the actual result matches the expected result.
        Logs success or failure and takes a screenshot in case of failure.
        """
        try:
            assert actual_result == expected_result, "The result does not match"
            self.logs.info(f"Assertion passed: Actual = {actual_result}, Expected = {expected_result}")
        except Exception as E:
            self.logs.error(f"Exception occurred while matching the data: {E}")
            self.take_screenshot()

    def switch_to_window(self):
        """
        Switches to the second browser window (newly opened tab or window).
        Useful when actions result in opening new browser windows.
        """
        try:
            windows = self.driver.window_handles
            self.driver.switch_to.window(windows[1])
            self.logs.info("Switched to new window successfully.")
        except Exception as E:
            self.logs.error(f"Exception occurred while switching window: {E}")
            self.take_screenshot()

    def clear_text(self, by_locator):
        """
        Clears the input field's current text.
        Useful before entering new input values.
        """
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator)).clear()
            self.logs.info(f"Cleared text of element located by: {by_locator}")
        except Exception as E:
            self.logs.error(f"Exception occurred while clearing: {E}")
            self.take_screenshot()

    def text_displayed(self, by_locator):
        """
        Checks if an element is visible on the screen.
        Returns True if the element is visible, False otherwise.
        """
        try:
            is_visible = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).is_displayed()
            self.logs.info(f"Element {by_locator} is displayed: {is_visible}")
            return is_visible
        except Exception as E:
            self.logs.error(f"Exception occurred while checking if element is displayed: {E}")
            self.take_screenshot()
