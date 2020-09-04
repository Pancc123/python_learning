import requests

url = 'http://openapi3.smarteoc.com'
header = {'Content-Type': 'application/x-www-form-urlencoded','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) /'
                                                              'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626./'
                                                              '121 Safari/537.36'}
payload = {'signatureMethod': 'HMAC-SHA256',
           'signatureVersion': '1.0',
           'accessKeyId':  'MTQ=',
           'timestamp': '1563776840043',
           'action': 'queryLatestMetricDatum',
           'version': '3.2.0',
           'pointId': '91253948345770090,91253948345770089,91253948345770091',
           'signature': '6h/yES8OlCUK/5ign/r9w/RHmSFQ4JBzniz70mH80n4='}

payload=payload.encode('utf-8')
with urllib.request.urlopen(url, header,payload) as f:
	print(f.read().decode('utf-8'))