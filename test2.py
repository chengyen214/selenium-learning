from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
 
 
options = Options()
options.add_argument("--disable-notifications")
 
chrome = webdriver.Chrome('./chromedriver', chrome_options=options)
chrome.get("https://www.ptt.cc/bbs/Stock/index.html")
link = chrome.find_element(By.LINK_TEXT,"‹ 上頁")
print(3)
link.click()
print(4)
tags=chrome.find_elements(By.CLASS_NAME,"title")
print(1)

for tag in tags:
    print(tag.text)
print(2)


chrome.close()