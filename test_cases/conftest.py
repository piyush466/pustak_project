

from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options

from page_object.Login_page import Login
from page_object.Product_Page import Product_Page
from test_cases.baseclass import BaseClass
from uihelper.helper_file import UI_Helper


@pytest.fixture()
def setup(request):
    option = Options()
    option.add_argument("--headless")
    option.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=option)
    driver.get("https://www.mypustak.com/")
    driver.implicitly_wait(10)
    request.cls.driver = driver
    request.cls.login = Login(driver)
    request.cls.uihelp = UI_Helper(driver)
    request.cls.pro_page = Product_Page(driver)

    yield driver
    driver.quit()

