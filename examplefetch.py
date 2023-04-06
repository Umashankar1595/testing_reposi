import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/")
time.sleep(5)
driver.find_element(By.XPATH,"//span[.='Downloads']").click()
time.sleep(5)
latest_text = driver.find_element(By.LINK_TEXT,'Latest stable version')
version = latest_text.text
print(version)
time.sleep(5)