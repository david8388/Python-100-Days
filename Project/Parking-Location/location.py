import requests

data = requests.get('http://parkinglocation.tbkc.gov.tw/getjson.ashx').json()

for item in data:
    print(item['停車場名稱'])