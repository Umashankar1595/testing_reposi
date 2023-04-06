import time

from selenium import webdriver
from selenium.common import NoAlertPresentException

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demoqa.com/")

time.sleep(2)
try:

    driver.find_element(By.XPATH, "//div[@class='card-up']").click()
    time.sleep(5)
    alert = driver.switch_to.alert.accept()
except NoAlertPresentException:
    print("no alert present")