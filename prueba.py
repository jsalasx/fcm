import requests
import json
url = "http://131.196.8.4:8001/ShowToken/"


_headers = {'Content-Type': 'application/json'}

response = requests.get(url=url, headers=_headers)
print(response.text)
data = json.loads(response.text)





