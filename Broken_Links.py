import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib3 import request

driver = webdriver.Chrome()
driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

#alllinks
allLinks=driver.find_elements(By.TAG_NAME,'a')
count=0
for link in allLinks:
    url=link.get_attribute('href')
    try:
        res=requests.head(url)
    except:
        None
    if res.status_code >=400:
        print(url,"is the broken link")
        count+=1
    else:
        print(url," is the valid link")
print("Total number of broken links:", count)
driver.close()