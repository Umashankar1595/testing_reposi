import time

from selenium import  webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.ajio.com/")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.XPATH,"//input[@placeholder='Search AJIO']").send_keys("shirts")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(10)
print("test complete succesfull")