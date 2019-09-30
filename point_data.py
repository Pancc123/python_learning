import requests

url='http://openapi3.smarteoc.com/metricDatum '
form_data = {
    'signatureMethod':'HMAC-SHA256&signatureVersion=1.0',
    'accessKeyId':'MTQ%3D',
    'timestamp':'1557746853620',
    'action':'queryLatestMetricDatum',
    'version':'3.2.0',
    'pointIds':'152046816542621696',
    'signature':'2wkclzd%2FjwtNPaImGUwCe88x57hvxLNC2WNu7nosVg0%3D'}

header = {
     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
     'Content-Type': 'application/x-www-form-urlencoded',
     'Referer': 'http://10.1.170.153:3000/openapi-test'

}

response = requests.post(url, data=form_data, headers=header)
print(response.status_code)