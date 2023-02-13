from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
 
 
options = Options()
options.add_argument("--disable-notifications")
 
chrome = webdriver.Chrome('./chromedriver', chrome_options=options)
chrome.get("https://www.nccu.edu.tw/app/home.php")
tags=chrome.find_elements(By.CLASS_NAME,"mbox")
print(1)
for tag in tags:
    print(tag.text)
print(2)
#link = chrome.find_element(By.LINK_TEXT,"政大人")
print(3)
#link.click()
print(4)

chrome.close()