from tabnanny import check

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("http://total-qa.com/checkbox-example/#google_vignette")
driver.maximize_window()

#Selecting Specific Checkbox

driver.find_element(By.XPATH,"//div[@id='primary']//input[1]").click()

#Selecting all checkboxes
driver.find_element(By.XPATH,"//div[@id='primary']//input[1]").click()
checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
print(checkboxes)
print(len(checkboxes))
for i in range(len(checkboxes)):
    checkboxes[i].click()

 # Clearing all the checkboxes
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()

#selecting first two checkboxes
for i in range(len(checkboxes)):
    if i<2:
        checkboxes[i].click()

for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()

#selecting last two checkboxes

for i in range(len(checkboxes)-2,len(checkboxes)):
     checkboxes[i].click()
time.sleep(5)
content = driver.find_element(By.XPATH,"//div[@class='entry-content']")
print(content.text)
driver.close()
