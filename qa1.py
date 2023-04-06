import time

from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.meesho.com/")
time.sleep(5)
driver.close()
print("meesho website is open")