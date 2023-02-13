from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from bs4 import BeautifulSoup as Soup
import time
 
options = Options()
options.add_argument("--disable-notifications")
url = 'https://www.nccu.edu.tw/app/home.php'
chrome = requests.get(url) 
# chrome = webdriver.Chrome('./chromedriver', chrome_options=options)
# chrome.maximize_window()
# chrome.requests.get("https://www.nccu.edu.tw/app/home.php")
soup = Soup(chrome.text,'html5lib') #將chrome.text內容定義到Beautifulsoup物件
path = 'chrome.txt'
f = open(path, 'w')
title = soup.find('a', class_='dropdown-toggle')
print(title.getText())
title2 = soup.find(title="行政單位")
print(title2)
print(chrome.text,file=f) #output <class 'bs4.BeautifulSoup'>
f.close()
