import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# time.sleep(5)
# driver.find_element(By.XPATH,"//button[@onclick='jsAlert()']").click()
# driver.find_element(By.XPATH,"//button[@onclick='jsConfirm()']").click()
# driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']").click()
# alert_obj = driver.switch_to.alert
# time.sleep(1)
# alert_obj.send_keys("simple txt")
# alert_obj.accept()
# alert_obj.dismiss()

# alert_obj = driver.switch_to.alert
# msg = alert_obj.text
# print(msg)
driver.get("https://www.google.com")
time.sleep(5)
driver.execute_script("window.open('https://yahoo.com')")
time.sleep(5)
windows = driver.window_handles
# for w in windows:
#     print(driver.current_window_handle)
google = windows[0]
yahoo = windows[1]
driver.switch_to.window(yahoo)
time.sleep(10)
driver.switch_to.window(google)
time.sleep(10)

