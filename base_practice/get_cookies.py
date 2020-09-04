# -*-coding:utf-8 -*-

from selenium import webdriver


driver = webdriver.Chrome()
driver.get("http://10.1.170.153:3000")
cookies = driver.get_cookies()
print(cookies)
driver.quit()
'''url = 'http://openapi3.smarteoc.com/management3761_32'
form_data = {
    'signatureMethod':'HMAC-SHA256&signatureVersion=1.0',
    'accessKeyId':'MTQ%3D',
    'timestamp':'1557746853620',
    'action':'queryLatestMetricDatum',
    'version':'3.2.0',
    'pointIds':'152046816542621696',
    'signature':'2wkclzd%2FjwtNPaImGUwCe88x57hvxLNC2WNu7nosVg0%3D'
           }
cookies = {'io': 'Vo5mAhL7hZIzAG0DACPW'}
header = {'Content-Type': 'application/x-www-form-urlencoded','Referer': 'http://10.1.170.153:3000/openapi-test',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
          Chrome/72.0.3626.121 Safari/537.36'}

response = requests.post(url, data=form_data, headers=header, cookies=cookies)
print(response.text)'''
