import time
from os import times


from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
option = Options()
option.add_argument("--start-maximized")
driver = webdriver.Chrome(options=option)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(10)
element = driver.find_element(By.XPATH, "//h2[text()='Slider']")
driver.execute_script("arguments[0].scrollIntoView();", element)

slider = driver.find_element(By.ID, "slider-range")
action = ActionChains(driver)
action.click_and_hold(slider).move_by_offset(200,600).release().perform()
time.sleep(4)













# images= driver.find_elements(By.TAG_NAME, "img")
#
# for img in images:
#     print(img)
#     is_broken = driver.execute_script("return arguments[0].naturalWidth == 0;", img)
#     if is_broken:
#         print(f"Broken Image Found: {img.get_attribute('src')}")



















# wait = WebDriverWait(driver,10)
# number = wait.until(EC.presence_of_element_located((By.XPATH, "//*[(text()='Input: Number')]/parent::div/input"))).send_keys(3)
# text = wait.until(EC.presence_of_element_located((By.XPATH, "//*[(text()='Input: Password')]/parent::div/input"))).send_keys("piyush234")
# password = wait.until(EC.presence_of_element_located((By.XPATH, "//*[(text()='Input: Text')]/parent::div/input"))).send_keys("piyush")
# date = wait.until(EC.presence_of_element_located((By.XPATH, "//*[(text()='Input: Date')]/parent::div/input"))).send_keys("12-12-2025")
# wait.until(EC.presence_of_element_located((By.XPATH, "//*[(text()='Display Inputs')]"))).click()
# verify_password = wait.until(EC.presence_of_element_located((By.ID, "output-password"))).text
# assert verify_password == "piyush234", "failed"
#
# time.sleep(5)