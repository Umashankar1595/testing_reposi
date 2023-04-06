import time

from selenium import  webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.actitime.com/login.do")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.ID,"username").send_keys("admin")
driver.find_element(By.NAME,"pwd").send_keys("manager")
driver.find_element(By.ID,"loginButton").click()
time.sleep(10)
driver.back()
print("test complete succesfull")
