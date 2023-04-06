from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/register")
try:
    driver.find_element(By.ID,"name").send_keys("rose")
except NoSuchElementException as e:
    print("element not found..test failed")

# exam2

