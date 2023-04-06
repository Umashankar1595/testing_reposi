from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

# set up the driver
driver = webdriver.Chrome()

# open the website
driver.get('http://www.demo.actitime.com/')

# enter login details and submit
driver.find_element(By.NAME,"username").send_keys("admin")
driver.find_element(By.NAME,"pwd").send_keys("manager")
driver.find_element(By.ID,"loginButton").click()

# click on the 'Tasks' tab
driver.find_element(By.ID,"container_tasks").click()

# click on 'Add New' button
driver.find_element(By.NAME,"downIcon").click()

# select 'New Customer' option
driver.find_element(By.XPATH,"//div[.='+ New Customer']").click()

# switch to the popup window
popup_window = driver.window_handles[1]
driver.switch_to.window(popup_window)

# enter customer details
driver.find_element(By.XPATH,"//input[@type='text']").send_keys('RAKESH')
driver.find_element(By.CLASS_NAME,"textarea").send_keys("Banking project")
Select(driver.find_element(By.NAME,"customerStatus")).select_by_visible_text('Active')
driver.find_element(By.CLASS_NAME,"components_button_label").click()

# switch back to the main window
driver.switch_to.window(driver.window_handles[0])

# verify the created customer
customer_name = driver.find_element(By.XPATH,"//a[@text()='RAKESH']").text
assert customer_name == 'RAKESH', f'Expected customer name: "RAKESH", got{customer_name}'

# click on the logout link
driver.find_element(By.ID,"logoutLink").click()

# quit the driver
driver.quit()