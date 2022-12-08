

import requests
import json


url="http://131.196.8.4:8001/ShowToken/"


_headers = {'Content-Type': 'application/json'}

response = requests.get(url=url,headers=_headers)

data = json.loads(response.text)

tokens = []
j = 0
while (j < len(data)):
    tokens.append(data[j]['token'])
    j=j+1
    


print(tokens)






