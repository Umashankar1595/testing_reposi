import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Open the browser and navigate to the ActiTime demo site
driver = webdriver.Chrome()
driver.get("https://demo.actitime.com/")

# Enter the username and password and click on the Login button
driver.find_element(By.ID, "username").send_keys("admin")
driver.find_element(By.NAME, "pwd").send_keys("manager")
driver.find_element(By.ID, "loginButton").click()
time.sleep(3)
# Click on the Tasks tab
driver.find_element(By.ID, "container_tasks").click()

# Click on the Add New button and select New Customer
driver.find_element(By.CSS_SELECTOR, ".addNewButton").click()
time.sleep(3)
driver.find_element(By.XPATH, "//div[.='+ New Customer']").click()

# Wait for the New Customer popup to appear and enter the customer details
wait = WebDriverWait(driver, 10)
customer_name = '2P13'
customer_desc = 'BANKING PROJECT'
customer_name_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='text']")))
customer_name_field.send_keys(customer_name)
driver.find_element(By.CSS_SELECTOR, "textarea[id='customerLightBox_descriptionField']").send_keys(customer_desc)

# Select the customer name from the drop-down and click on the Create Customer button
customer_dropdown = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#customerLightBox .dropdownButton")))
customer_dropdown.click()
customer_option = wait.until(EC.presence_of_element_located((By.XPATH, f"//div[@class='dropdownContainer active']//div[contains(text(), '{customer_name}')]")))
customer_option.click()
driver.find_element(By.CSS_SELECTOR, "div[id='customerLightBox_commitBtn']").click()

# Verify that the customer has been created
created_customer = wait.until(EC.presence_of_element_located((By.XPATH, f"//div[@class='customerNameDiv']//a[text()='{customer_name}']")))
assert created_customer.text == customer_name

# Click on the Logout button
driver.find_element(By.ID, "logoutLink").click()

# Close the browser
driver.quit()
