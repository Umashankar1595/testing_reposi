import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.actitime.com/login.do")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.ID,"username").send_keys("admin")
driver.find_element(By.NAME,"pwd").send_keys("manager")
driver.find_element(By.ID,"loginButton").click()
time.sleep(5)
driver.find_element(By.ID,"container_tasks").click()
time.sleep(8)
driver.find_element(By.XPATH,"//input[@placeholder='Start typing name ...']").send_keys("flight")
time.sleep(8)
driver.find_element(By.ID,"container_reports").click()
time.sleep(5)
driver.find_element(By.XPATH,"//div[@class='config-name']").click()
time.sleep(5)
driver.find_element(By.ID,"logoutLink").click()
time.sleep(10)
driver.find_element(By.LINK_TEXT,"Forgot your password?").click()
time.sleep(5)