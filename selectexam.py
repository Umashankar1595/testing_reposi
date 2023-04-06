import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("file:///C:/Users/R.K%20GOWDA/Desktop/drop.html")
# drp_down = driver.find_element(By.ID,"weekdaysmenu")
# select = Select(drp_down)
# time.sleep(1)
# select.select_by_index(4)
# time.sleep(1)
# select.select_by_visible_text("Saturday")
# time.sleep(2)
# select.select_by_value("5")
# time.sleep(2)
cars = Select(driver.find_element(By.ID, "cars"))
time.sleep(5)
# list1 = cars.all_selected_options
# for l in list1:
#     print(l.text)
# list2 = cars.first_selected_option
# option = cars.options
# for i in option:
# print(list2.text)
list3 = cars.all_selected_options
opt = cars.options
for i in opt:
    print(i.text)
