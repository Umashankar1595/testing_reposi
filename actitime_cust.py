import time


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.actitime.com/")
driver.maximize_window()
driver.find_element(By.NAME,"username").send_keys("admin")
driver.find_element(By.NAME,"pwd").send_keys("manager")
driver.find_element(By.ID,"loginButton").click()
time.sleep(5)
driver.find_element(By.ID,"container_tasks").click()
time.sleep(5)
driver.find_element(By.CLASS_NAME,"downIcon").click()
time.sleep(5)
driver.find_element(By.XPATH,"//div[.='+ New Customer']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//input[@class='inputFieldWithPlaceholder newNameField inputNameField']").send_keys("Raki")
time.sleep(3)
driver.find_element(By.XPATH,"//textarea[@placeholder='Enter Customer Description']").send_keys("Banking project")
time.sleep(2)
driver.find_element(By.XPATH,"//div[.='- Select Customer -']/div[@class='emptySelection']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//div[@class='searchItemList']/div[.='Big Bang Company']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//div[@class='components_button withPlusIcon']").click()

time.sleep(2)
driver.find_element(By.XPATH,"//a[.='Logout']").click()