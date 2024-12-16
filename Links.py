from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

#Locating links

driver.find_element(By.LINK_TEXT,"Digital downloads").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"Digital").click()

#Find number of links in a page
links= driver.find_elements(By.TAG_NAME,"a") #approach1
#links= driver.find_elements(By.XPATH,"//a") #alternative approach2
print("total num of links:", len(links))

#print all link names
for link in links:
    print(link.text)
driver.close()

