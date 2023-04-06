import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")
# images = driver.find_elements(By.TAG_NAME,"img")
# print("total number of images", len(images))
# print(f'There are {images} images on the page.')

driver.find_element(By.XPATH,"//input[@aria-label='Search Amazon.in']").send_keys("iphone14")
time.sleep(3)
driver.find_element(By.ID,"nav-search-submit-button").click()
time.sleep(2)
driver.find_element(By.XPATH,"//span[text()='71,999'][1]")
time.sleep(5)

