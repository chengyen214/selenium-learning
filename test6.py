from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from bs4 import BeautifulSoup as Soup
import time
 
options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
 
driver = webdriver.Chrome('./chromedriver', chrome_options=options)
driver.maximize_window()
driver.get("https://www.nccu.edu.tw/app/home.php")

time.sleep(3)
#$signinbtm=chrome.find_element(By.XPATH,"//*[@id='Hln_17']")
signinbtm=driver.find_element(By.ID,"Hln_14")
signinbtm.click()    #點擊登入
print(driver.current_url)

#chrome.back()
chrome= requests.get(driver.current_url)
soup = Soup(chrome.text,'html5lib')# for tag in tags:
#     tag.click()
for i in range(2):
    btm=driver.find_element(By.LINK_TEXT,"中國文學系")
    btm.click()    #點擊登入
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
time.sleep(2)
driver.close()
# driver.back()
# path = '政大.txt'
# f = open(path, 'w')
# print(chrome.text,file=f)
# f.close()
# titles = soup.find_all(target="_blank")
# for title in titles:
#     print(title.getText())
# print('\n\n')
# driver.back()
# time.sleep(3)


# signinbtm=driver.find_element(By.ID,"Hln_14")
# signinbtm.click()

# #search=chrome.find_element(By.PARTIAL_LINK_TEXT,"成績查詢")
# #search.send_keys(Keys.ENTER)
# time.sleep(3)
# chrome= requests.get(driver.current_url)
# soup = Soup(chrome.text,'html5lib')
# path = '政大2.txt'
# f = open(path, 'w')
# print(chrome.text,file=f)
# f.close()
# titles = soup.find_all(target="_blank")
# for title in titles:
#     print(title.getText())
# time.sleep(3)
# # chrome.forward()
# # time.sleep(3)
# chrome.close()