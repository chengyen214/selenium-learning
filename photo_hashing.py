import os
from PIL import Image
import imagehash

def checkImage(hashedImage,check_image):
    print(hashedImage)
    print(check_image)
    hash1=imagehash.average_hash(Image.open(hashedImage))
    print(hash1)
    img = Image.open(hashedImage)
    img.show()
    hash2=imagehash.average_hash(Image.open(check_image))
    print(hash2)
    img = Image.open(check_image)
    img.show()
    if hash1 == hash2:
        print("Same image")
    else:
        print("Not the same image")
# path='department.txt'
# file = open(path, "r",encoding="utf-8")
# departments=file.read()
# departments_data=departments.split("\n")
# departments_data.pop()
# print(departments_data)
# file.close()
# path='check_time.txt'
# file = open(path, "r",encoding="utf-8")
# check_time=file.read()
# check_time_data=check_time.split("\n")
# check_time_data.pop()
# print(check_time_data)
# file.close()
# for department_data in departments_data:
#     hashedImage=department_data+check_time_data[0]+'.png'
#     check_image=department_data+check_time_data[1]+'.png'
#     checkImage(hashedImage,check_image)