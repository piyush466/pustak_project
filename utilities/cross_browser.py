from selenium import  webdriver

import pytest

from utilities.broken_links import driver


def pytest_addoption(parser):
    parser.addoption("--new_browser", default="chrome", action="store")


@pytest.fixture
def setup(request):
    brwoser = request.config.getoption("--new_browser")

    if brwoser == "chrome":
        driver = webdriver.Chrome()

    elif brwoser == "firefox":
        driver = webdriver.Firefox()

    else:
        driver = webdriver.Chrome()

    driver.get("https://www.mypustak.com/")
