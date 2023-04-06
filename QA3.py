import time

from selenium import  webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(8)
driver.refresh()
# driver.execute_script("window.open('https://www.youtube.com')")
# driver.get_screenshot_as_file('youtube.png')
# time.sleep(10)
# driver.quit()
# driver.maximize_window()
# time.sleep(5)
# driver.find_element(By.NAME,"username").send_keys("student")
# driver.find_element(By.NAME,"password").send_keys("Password123")
# driver.find_element(By.ID,"submit").click()
# time.sleep(10)
# driver.back()
# time.sleep(10)
# driver.forward()
# time.sleep(5)
print("test complete succesfull")
