# import requests module
import requests

# Making a get request
def url_checker(url):
    try:
        #Get Url
        get = requests.get(url)
        return(get.status_code )
        #Exception
    except requests.exceptions.RequestException :
            # print URL with Errs
            wrong=0
            return(wrong)

url='https://tailit.nccu.edu.tw/Page1Doc?fid=2104'
print(url_checker(url))