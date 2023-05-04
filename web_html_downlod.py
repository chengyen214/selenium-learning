from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.service import Service
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
import imagehash
import requests
from bs4 import BeautifulSoup as Soup
import time
import ssl
import certifi
from urllib.request import urlopen
import re
import time
import requests
import urllib.request
import hashlib
from sql_insert import return_value,chronology_insert,link_insert,UPDATE_value
import sql_insert
import datetime
import error_test

def storelink(links,name):
    link_f = open(name, 'w', encoding='UTF-8')
    for l in links:
        print(l,file=link_f)
    f.close()

def replace_all_blank(value):
    result = re.sub('\W+', '', value).replace("_", '')
    # print(result)
    return result

request = "https://example.com"
urlopen(request, context=ssl.create_default_context(cafile=certifi.where()))


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
departments=[]
chrome= requests.get(driver.current_url)
soup = Soup(chrome.text,'html5lib')
tags=soup.find_all('a',target="_blank")
# i=0
# for tag in tags:
#     if i > 2:
#         departments.append(tag.getText().strip())
#     i+=1
# for i in range(7):
#     departments.pop()
departments = ['中國文學系','歷史學系','哲學系']

# path = 'departments.txt'
path = 'department.txt'
f = open(path, 'w', encoding='UTF-8')
for department in departments:
    f.write(department+'\n')
f.close()
path = 'check_time.txt'
time_f = open(path, 'w', encoding='UTF-8')
Time=[]

values=return_value()
record_aomount=values[1]
link_amount=values[2]

for x in range(1,3):
    record_aomount+=1
    
    print(record_aomount)
    driver.get("https://www.nccu.edu.tw/p/426-1000-55.php?Lang=zh-tw")
    time.sleep(3)
    localtime = time.localtime()
    Now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #store name
    now_time= str(time.strftime("%Y-%m-%d-%I%M%S", localtime))
    Time.append(now_time)
    time_f.write(now_time+'\n')
    chronology_insert(record_aomount,Now)

    Status_codes=[]
    for department in departments:
        url2=driver.find_element(By.LINK_TEXT,department).get_attribute('href')
        response = error_test.url_checker(url2)
        Status_codes.append(response)
    print('Status_codes:')
    print(Status_codes)
    # print(len(Status_codes),len(departments))
    #check each department
    
    for (department,status) in zip(departments,Status_codes):
        name=re.sub('[^\u4e00-\u9fa5]+','',department)
        Now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if status==200:
            btm=driver.find_element(By.LINK_TEXT,department)
            btm.click()
            btm.get_attribute('href')
            time.sleep(10)
            driver.switch_to.window(driver.window_handles[1])
            path = name+'-'+now_time+'.txt'
            f = open(path, 'w', encoding='UTF-8')
            html1= driver.page_source
            soup = Soup(html1,'html5lib')
            html1=str(html1)
            print(html1,file=f)
            f.close()

            # photo download
            photo_addr=driver.find_element(By.XPATH,'//*[@alt="logo"]').get_attribute('src')
            photo_url=photo_addr
            print(photo_url)
            print(department)
            photo=name+now_time+'.png'
            urllib.request.urlretrieve(photo_url,photo)

            #sql_insert
            hash1=imagehash.average_hash(Image.open(photo))
            # hash2=hashlib.md5()
            # hash2.update(html1.encode('utf-8'))
            # hash2.hexdigest()
            # print(type(hash2))

            sql_insert.sql_data_insert(department,Now,html1,hash1)

            

            #used_url_insert
            link=[]
            type=[]
            links=driver.find_elements(By.XPATH,'//*[@href]')
            for l in links:
                ll=l.get_attribute('href')
                if ll :
                    link.append(ll)
                    type.append('href')
            links2=driver.find_elements(By.XPATH,'//*[@src]')
            # link.append('ll')
            for l in links2:
                # print(l.text)
                ll=l.get_attribute('src')
                if ll != None:
                    link.append(ll)
                    type.append('src')

            titles=driver.find_elements(By.XPATH,'//*[@title]')
            for t in titles:
                title=t.get_attribute('title')
                if title != None:
                    link.append(title)
                    type.append('title')


            alts=driver.find_elements(By.XPATH,'//*[@alt]')
            for t in alts:
                alt=t.get_attribute('alt')
                if alt != None:
                    link.append(alt)
                    type.append('title')

            p2=driver.find_elements(By.TAG_NAME,'p')
            for p in p2:
                if not replace_all_blank(p.text) :               
                    link.append( replace_all_blank(p.text))
                    type.append('p')
            # print(p[1])

            link_file='link_'+name+now_time+'.txt'
            storelink(link,link_file)

            for (ll,ty) in zip(link,type):
                link_amount+=1
                link_insert(link_amount,name,Now,ll,ty)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(2)
            sql_insert.sql_commit()
        else:
            sql_insert.HTTP_Status_warning(name,Now,status)
        UPDATE_value(record_aomount,link_amount)
        sql_insert.sql_commit()
    

import web_comparison

for department in departments:
    name=re.sub('[^\u4e00-\u9fa5]+','',department)
    file1='link_'+name+Time[0]+'.txt'
    file2='link_'+name+Time[0]+'.txt'
    web_comparison.filecompare(file1,file2,department)
    

time_f.close()
sql_insert.sql_commit()

print(departments)
driver.close()

