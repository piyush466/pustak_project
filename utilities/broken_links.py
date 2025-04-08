

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import requests
option = Options()
option.add_argument("--start-maximized")
driver = webdriver.Chrome(options=option)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(10)
links = driver.find_elements(By.TAG_NAME, "a")
#
# for link in links:
#     url = link.get_attribute("href")
#     # print(url)
#     if url:
#         try:
#             response = requests.get(url)
#             if response.status_code>=400:
#                 print(f"this is broken link {url}", f"and status code is {response.status_code}")
#             else:
#                 print(f"this is valid {url}",f"and status code is {response.status_code}")
#         except Exception as E:
#             print("Exception", E)
#
#
#
#
