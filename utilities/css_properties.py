from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(10)
size_of_title = "40px"
element = driver.find_element(By.XPATH, "//h1[1]")

font_match = element.value_of_css_property("font-size")
print(font_match)
color = element.value_of_css_property("color")
print(color)
location = element.location["x"]
print(location,"xlocation")
ylocation = element.location["y"]
print("ylocation", ylocation)
assert font_match == size_of_title, "Font size is not match"
