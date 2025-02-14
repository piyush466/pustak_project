import time


from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from uihelper.helper_file import UI_Helper

from selenium.webdriver.support import expected_conditions as EC
class Product_Page(UI_Helper):

    SEARCH_PRODUCT_XPATH = (By.XPATH, "(//input[@id='gsearch'])[1]")
    CLICK_ON_SEARCH_BTN_XPATH = (By.XPATH, '(//button[@aria-label="searchButton"])[1]')
    VALIDATE_WITH_THE_BOOK_CSS = (By.CSS_SELECTOR, "[class='jsx-45b79a600e3d4efb clearButton']")
    CLICK_ON_BUY_NOW_XPATH = (By.XPATH, "(//*[text()='Buy Now'])[1]")
    CAPTURE_THE_BOOK_NAME = (By.CLASS_NAME, "CartPage_cartBookTitle__BCliw")
    #CLick on add to cart button
    CLICK_ON_ADD_TO_CART_BTN_XPATH = (By.XPATH, "//div[@class='jsx-313054587 md:h-[29.5rem] w-[100%] h-[30.5rem]  bg-white flex flex-col']/div[4]/button")
    CLICK_ON_CART_XPATH = (By.XPATH, "(//span[text()='Cart'])[1]")
    VERIFY_TEXT_OF_CART_CSS = (By.CSS_SELECTOR, "[class='px-3']")


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
        time.sleep(2)
        self.do_click(self.CLICK_ON_BUY_NOW_XPATH)
        self.book_name = self.get_text(self.CAPTURE_THE_BOOK_NAME)
        # self.book_name = ""
        self.title_case = self.book_name.title()
        time.sleep(4)

    def multiple_product_add_cart(self):
        self.buttons = self.driver.find_elements(By.XPATH, "//button[text()='Add to Cart']")

        for button in self.buttons[:3]:  # Use 'button' instead of 'self.button'

            try:
                add_to_cart_popup = self.driver.find_element(By.XPATH, "(//div[text()='Add to Cart'])[2]")
                button.click()
                time.sleep(2)
                if add_to_cart_popup.is_displayed():
                    time.sleep(2)
                    add_to_cart_popup.click()
                    time.sleep(2)

            except Exception as E:  # Catch only NoSuchElementException
                print("Add to Cart popup not found. Continuing...", E)

        # self.do_click(self.CLICK_ON_CART_XPATH)
        self.driver.find_element(By.XPATH, "(//span[text()='Cart'])[1]").click()
        time.sleep(3)
        self.verify_text = self.driver.find_element(By.CSS_SELECTOR, "[class='px-3']").text

    def remove_all_products(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, "(//span[text()='Cart'])[1]").click()
        wait = WebDriverWait(self.driver, 10)

        while True:
            try:
                # Find the first available Remove button
                remove_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Remove']")))
                remove_button.click()
                print("Clicked Remove")

                # Wait for Yes button and click
                yes_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Yes']")))
                yes_button.click()
                print("Clicked Yes")

                time.sleep(2)  # Wait for changes in the DOM

            except StaleElementReferenceException:
                print("Element became stale. Retrying...")
                time.sleep(1)
                continue

            except Exception as e:
                print("No more Remove buttons found. Exiting loop.")
                break  # Exit loop when no more elements are found


    def add_filter(self):
        self.all_authors = self.driver.find_elements(By.XPATH, "//label[@style='cursor: pointer;']")

        for author in self.all_authors:
            if author.text == "Dr V K Sharma(7)":
                author.click()
                break

        self.applied_filter_author = self.driver.find_elements(By.XPATH, "//h2[@title='dr v k sharma']")
        print(len(self.applied_filter_author))
        for applied_author in self.applied_filter_author:
            print(applied_author.text)
            self.author = f'By {"Dr V K Sharma"}'
            if applied_author.text == self.author:
                print("Test is passed")
                break
            else:
                print("Test is Failed")
        time.sleep(4)


    def sub_links(self):
        for _ in range(3):
            self.driver.execute_script("window.scrollBy(0, 15000)")
            time.sleep(2)

        self.all_links = self.driver.find_elements(By.XPATH, "//li[@class='jsx-38dabb2c740aff62']")
        self.capture_list = []
        self.after_click_on_link = []
        for link in self.all_links:
            text = link.text
            self.capture_list.append(text)
            try:
                link.click()
                time.sleep(2)
                window = self.driver.window_handles
                self.driver.switch_to.window(window[1])
                if self.driver.find_element(By.XPATH, "(//img)[1]").is_displayed():
                    print("This link is displayed:- ",f"{text}")
                    self.after_click_on_link.append(text)
                    self.driver.switch_to.window(window[0])
                else:
                    print("This link is not displayed:- ",f"{text}")
                    self.driver.switch_to.window(window[0])
            except Exception as E:
                print(E)
                raise







