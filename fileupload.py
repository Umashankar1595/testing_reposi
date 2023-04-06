import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
file_input = driver.get("https://the-internet.herokuapp.com/upload")
time.sleep(5)
file_path = r"C:\Users\R.K GOWDA\Downloads\add.pdf"
time.sleep(5)
driver.find_element(By.ID, "file-upload").send_keys(file_path)
time.sleep(3)

driver.find_element(By.ID, "file-submit").click()

if driver.page_source.find("file uploaded"):
    print("file upload sucess")
else:
    print("not upload")
