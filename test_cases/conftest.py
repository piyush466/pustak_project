from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from page_object.Checkout_Page import Checkout_Page
from page_object.Login_page import Login
from page_object.My_Profile_page import My_Profile
from page_object.Product_Page import Product_Page
from page_object.wishlist_page import WishListPage
from test_cases.baseclass import BaseClass
from test_data import Login_creds
from uihelper.helper_file import UI_Helper
import configparser

config = configparser.ConfigParser()
config.read(Login_creds.path_of_config_file)

@pytest.fixture()
def setup(request):
    option = Options()
    # option.add_argument("--headless")
    option.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=option)
    driver.get(config["URL"]["URL"])
    driver.implicitly_wait(10)
    request.cls.driver = driver
    request.cls.login = Login(driver)
    request.cls.uihelp = UI_Helper(driver)
    request.cls.pro_page = Product_Page(driver)
    request.cls.checkout = Checkout_Page(driver)
    request.cls.my_profile = My_Profile(driver)
    request.cls.wishl = WishListPage(driver)

    yield driver
    driver.quit()

