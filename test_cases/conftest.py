import pytest
import configparser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from page_object.Checkout_Page import Checkout_Page
from page_object.Login_page import Login
from page_object.My_Profile_page import My_Profile
from page_object.Product_Page import Product_Page
from page_object.wishlist_page import WishListPage
from uihelper.helper_file import UI_Helper
from test_data import Login_creds

# Load config
config = configparser.ConfigParser()
config.read(Login_creds.path_of_config_file)


def pytest_addoption(parser):
    parser.addoption(
        "--newbrowser", action="store", default="chrome", help="Browser to use"
    )
    parser.addoption(
        "--url", action="store", default=config["URL"]["URL"], help="URL to test"
    )


@pytest.fixture()
def setup(request):
    browser = request.config.getoption("--newbrowser")
    url = request.config.getoption("--url")

    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)

    elif browser == "firefox":
        options = FirefoxOptions()
        options.add_argument("--headless")
        options.add_argument("--start-maximized")
        driver = webdriver.Firefox(options=options)


    else:
        raise Exception("Unsupported browser: Choose 'chrome' or 'firefox'")

    options.add_argument("--headless")
    driver.get(url)
    driver.implicitly_wait(10)

    # Attach everything to the class
    request.cls.driver = driver
    request.cls.login = Login(driver)
    request.cls.uihelp = UI_Helper(driver)
    request.cls.pro_page = Product_Page(driver)
    request.cls.checkout = Checkout_Page(driver)
    request.cls.my_profile = My_Profile(driver)
    request.cls.wishl = WishListPage(driver)

    yield driver
    driver.quit()
