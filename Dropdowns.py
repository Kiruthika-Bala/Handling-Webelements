import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
driver.maximize_window()

date_ele= Select(driver.find_element(By.XPATH,"//select[@name='DateOfBirthDay']"))
month_ele = Select(driver.find_element(By.XPATH,"//select[@name='DateOfBirthMonth']"))
year_ele=Select(driver.find_element(By.XPATH,"//select[@name='DateOfBirthYear']"))

#select option from the dropdown
date_ele.select_by_index(30)
month_ele.select_by_visible_text("October")
year_ele.select_by_value("1998")


#count all the options from the dropdown

alloptions= date_ele.options
print("Total no of Date options:",len(alloptions))

#Select options from dropdown without using built in method

for opt in alloptions:
    if opt.text=="10":
        opt.click()
        break
time.sleep(5)

