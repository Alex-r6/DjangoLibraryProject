import requests

URL = 'http://127.0.0.1:8000/api/author/list/'

data = requests.get(URL).json()
for item in data:
    print(item['__str__'])
# print(data)