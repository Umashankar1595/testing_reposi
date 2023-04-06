import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.linkedin.com/home")
time.sleep(5)
driver.find_element(By.NAME,"session_key").send_keys("umashankark1595@gmail.com")
driver.find_element(By.NAME,"session_password").send_keys("Rakesh@123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(10)
title = driver.title
curl = driver.current_url
print("this is the page title", title)
print("this is the current url", curl)
