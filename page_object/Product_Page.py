import time
from tkinter import Scale

from selenium.webdriver.common.by import By

from uihelper.helper_file import UI_Helper


class Product_Page(UI_Helper):

    SEARCH_PRODUCT_XPATH = (By.XPATH, "(//input[@id='gsearch'])[1]")
    CLICK_ON_SEARCH_BTN_XPATH = (By.XPATH, '(//button[@aria-label="searchButton"])[1]')
    VALIDATE_WITH_THE_BOOK_CSS = (By.CSS_SELECTOR, "[class='jsx-45b79a600e3d4efb clearButton']")
    CLICK_ON_BUY_NOW_XPATH = (By.XPATH, "(//*[text()='Buy Now'])[1]")
    CAPTURE_THE_BOOK_NAME = (By.CLASS_NAME, "CartPage_cartBookTitle__BCliw")

    def __init__(self, driver):
        self.driver = driver

    def search_book(self,text):
        self.send_key(self.SEARCH_PRODUCT_XPATH, text)
        self.do_click(self.CLICK_ON_SEARCH_BTN_XPATH)

    def add_product_into_cart(self):
        self.search_book("Health Book")
        self.all_books = self.driver.find_elements(By.XPATH, "//h2[1]")
        # self.add_cart_buttons = self.driver.find_elements(By.CLASS_NAME, "jsx-313054587 flex items-center	 flex-col")
        for book in self.all_books:
            # print(book.text)
            # print(button.text)
            if book.text == "The World Book Health And Medical Annual 1993":
                book.click()
                # button.click()
                break
        self.switch_to_window()
        self.do_click(self.CLICK_ON_BUY_NOW_XPATH)
        self.book_name = self.get_text(self.CAPTURE_THE_BOOK_NAME)
        # self.book_name = ""
        self.title_case = self.book_name.title()
        time.sleep(4)



