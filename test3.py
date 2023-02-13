from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as Soup
import time
 
 
options = Options()
options.add_argument("--disable-notifications")
 
chrome = webdriver.Chrome('./chromedriver', chrome_options=options)
chrome.maximize_window()
chrome.get("https://i.nccu.edu.tw/Login.aspx?ReturnUrl=%2fHome.aspx")

usernameInput=chrome.find_element(By.ID,"captcha_Login1_UserName")
passwordInput=chrome.find_element(By.ID,"captcha_Login1_Password")
usernameInput.send_keys("109703032")
passwordInput.send_keys("a1031426")
signinbtm=chrome.find_element(By.ID,"captcha_Login1_LoginButton")
signinbtm.send_keys(Keys.ENTER)     #點擊登入
time.sleep(5)
#chrome.back()
soup = Soup(chrome.page_source, 'html.parser')# for tag in tags:
#     tag.click()
#search=chrome.find_element(By.PARTIAL_LINK_TEXT,"成績查詢")
#search.send_keys(Keys.ENTER)
time.sleep(3)
# chrome.forward()
# time.sleep(3)
#chrome.close()