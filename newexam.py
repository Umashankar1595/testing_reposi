from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("file:///C:/Users/R.K%20GOWDA/Desktop/new.html")
login1 = driver.find_element(By.XPATH,"/html/body/form[1]/input[2]")
login2 = driver.find_element(By.XPATH,"//input[2]")
login3 = driver.find_element(By.XPATH,"//input[@name='username']")
print(login1.get_attribute('outerHTML'))
print(login2.get_attribute('outerHTML'))
print(login3.get_attribute('outerHTML'))