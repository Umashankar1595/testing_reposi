import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()
driver.get("file:///D:/form.html")
driver.find_element(By.ID,"username").send_keys("rakesh")
time.sleep(2)
driver.find_element(By.ID,"password").send_keys("123456")
driver.find_element(By.XPATH,"//input[@value='male']").click()
# selection = Select(driver.find_element(By.XPATH, "//input[@list='Options']"))
# driver.find_element(By.XPATH, "//value='Option1']")
time.sleep(3)
# selection.select_by_index(1)
driver.find_element(By.NAME,"correct").click()
time.sleep(3)
driver.find_element(By.XPATH,"//input[@type='submit']").click()