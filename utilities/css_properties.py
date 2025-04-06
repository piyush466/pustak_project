from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
from utilities.logger import setup_logger
logs = setup_logger()
logs.info("opening bwoser")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(10)
size_of_title = "40px"
element = driver.find_element(By.XPATH, "//h1[1]")
driver.save_screenshot(r"C:\Users\Piyush Dravyakar\pythonProject_pustak\screenshots\piyush.png")

WebDriverWait(driver,10).until(EC.visibility_of_element_located(By.XPATH, "//h1[1]")).is_displayed()

# font_match = element.value_of_css_property("font-size")
# print(font_match)
# color = element.value_of_css_property("color")
# print(color)
# location = element.location["x"]
# print(location,"xlocation")
# ylocation = element.location["y"]
# print("ylocation", ylocation)
# assert font_match == size_of_title, "Font size is not match"
