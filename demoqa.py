import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.ID,"firstName").send_keys("rakesh")
driver.find_element(By.ID,"lastName").send_keys("pass")
driver.find_element(By.ID,"userEmail").send_keys("abc@gmail.com")
driver.find_element(By.XPATH,"//label[text()='Male']").click()
driver.find_element(By.ID,"userNumber").send_keys("7896541235")
time.sleep(3)
driver.find_element(By.ID,"dateOfBirthInput").click()
driver.find_element(By.XPATH,"//lable[.='Sports']").click()
driver.find_element(By.ID,"currentAddress").send_keys("bengaluru")
# driver.find_element(By.XPATH,"//div[.='Select State']").click()
driver.find_element(By.ID,"submit").click()
