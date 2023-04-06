from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.amazon.com/")
links = driver.find_elements(By.TAG_NAME,("a"))
print(links)