import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("file:///D:/demo1.html")
time.sleep(5)
# csselem = driver.find_element(By.CSS_SELECTOR, 'li.deer')
# print(csselem.get_attribute("outerHTML"))
#
# xpathelem = driver.find_element(By.XPATH,"/html/body/ul/li(1)")
# print(xpathelem.get_attribute("outerHTML"))
# xpathelem = driver.find_element(By.XPATH,"li[@class='bat']")
# print(xpathele.get_attribute("outerHTML"))

doglist =  Select(driver.find_element(By.ID,'dog-names'))
doglist.select_by_index(0)
time.sleep(5)
doglist.select_by_visible_text("Dave")
time.sleep(5)
doglist.select_by_value('reeses')
time.sleep(2)
