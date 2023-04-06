import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.com/maps")
time.sleep(3)
driver.find_element(By.ID,"searchboxinput").send_keys("Mysuru")
time.sleep(5)
driver.find_element(By.ID,"searchbox-searchbutton").click()
time.sleep(3)
driver.find_element(By.XPATH,"//img[@alt='Directions']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//input[@placeholder='Choose starting point, or click on the map...']").send_keys("Bengaluru")
time.sleep(3)
driver.find_element(By.XPATH,"//button[@data-tooltip='Search']").click()
time.sleep(3)
info = driver.find_element(By.ID,"section-directions-trip-0").text
time.sleep(2)
print(info)