import pymysql
import pymysql.cursors
import datetime
import time

# 資料庫參數設定
db_settings= {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "a1031426",
    "db": "html_check",
    "charset": "utf8"
}
conn = pymysql.connect(**db_settings)
cursor = conn.cursor()

def sql_data_insert(department,Now,html,photo_hash):
    command = "INSERT INTO department_html(department, create_time,html,photo_hash)VALUES(%s, %s,%s,%s)"
    cursor.execute(command,(department,Now,html,photo_hash))
    
def sql_commit():
    conn.commit()

# def sql_link_insert(department,Now,html,photo_hash):
#     command = "INSERT INTO department_html(department, create_time,html,photo_hash)VALUES(%s, %s,%s,%s)"

def return_value():
    command = "SELECT * FROM max_value WHERE Mid = 1"
    cursor.execute(command)
    results = cursor.fetchall()
    for result in results: 
        value=list(result)
    return value

def chronology_insert(Tid,creat_time):
    command = "INSERT INTO chronology(Tid, create_time)VALUES(%s, %s)"
    cursor.execute(command,(int(Tid),creat_time))



def link_insert(lid,department,Now,link,type):
    command = "INSERT INTO link_store(Lid,department,create_time,link,type)VALUES(%s, %s, %s, %s,%s)"
    cursor.execute(command,(int(lid),department,Now,link,type))

# lid=1
# department='中國文學系'
# Now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# link='https://chinese.nccu.edu.tw/assets/css/page.css'
# link_insert(lid,department,Now,link)
# print('success')

def UPDATE_value(record_aomount,link_amount):
    command = "UPDATE max_value SET record_amount = %s,link_amount=%s WHERE Mid = 1"
    cursor.execute(command,(int(record_aomount),int(link_amount)))

def HTTP_Status_warning(department,now,status):
    command = "INSERT INTO web_connect_error(web_err_depart,Web_Status_codes,)VALUES(%s, %s, %s)"
    cursor.execute(command,(department,now,int(status)))
    

# UPDATE_value(1,1)

# Now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# chronology_insert(1,Now)
# print(1)

def html_hash_compare():
    command = "SELECT * FROM max_value WHERE Mid = 1"
    cursor.execute(command)
    results = cursor.fetchall()
    for result in results: 
        value=list(result)
    command2 = "SELECT * FROM chronology WHERE Mid = (Tid)VALUES(%s)"
    cursor.execute(command2(value[1]))
    = cursor.fetchall()
# values=return_value()
# print(values[0],values[1],values[2])

# Now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# sql_data_insert('中國文學系',Now)
# sql_commit()
sql_commit()
