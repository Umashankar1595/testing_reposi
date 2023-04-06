import time

from selenium import  webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("file:///D:/!DOCTYPE.html#")
driver.find_element(By.XPATH,"//a[.='Home']").click()
time.sleep(3)
