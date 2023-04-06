import time

from selenium import  webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/upload")
driver.find_element(By.ID,"file-upload").send_keys("D:\samplee.txt")
driver.find_element(By.ID,"file-submit").submit()
time.sleep(5)

if driver.page_source.find("file uploaded"):
    print("upload succesfull")
else:
    print("not uploaded")