import time

from selenium import  webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.flipkart.com/")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.NAME,"q").send_keys("shoes")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(10)
print("test complete succesfull")