from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# Get all cookies
cookies = driver.get_cookies()
print(cookies)  # Prints a list of all cookies
print(cookies[0]["name"])
print(cookies[0]["value"])
print(cookies[0].values())
print(cookies[0].keys())

driver.quit()
