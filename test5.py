from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as Soup
import time
 
options = Options()
options.add_argument("--disable-notifications")
 
chrome = webdriver.Chrome('./chromedriver', chrome_options=options)
chrome.get("https://www.facebook.com/")
 
email = chrome.find_element(By.ID,"email")
password = chrome.find_element(By.ID,"pass")
 
email.send_keys('kuoat2013@yahoo.com')
password.send_keys('a901209901209')
password.submit()
 
time.sleep(3)
chrome.get('https://www.facebook.com/learncodewithmike')
 
for x in range(1, 3):
    chrome.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(5)
 
soup = BeautifulSoup(chrome.page_source, 'html5lib')
 
titles = soup.find_all('span', class_='x11i5rnm xat24cr x1mh8g0r x1vvkbs xdj266r x126k92a')
 
for title in titles:
 
    post = title.find('span', {'dir': 'auto'})
 
    if post:
        print(post.getText())
 
chrome.quit()