import fcmManager as fcm
import requests
import json
import time
from datetime import datetime


url="http://157.245.254.135/ShowToken/"


_headers = {'Content-Type': 'application/json'}

response = requests.get(url=url,headers=_headers)

data = json.loads(response.text)

tokens = []
j = 0
while (j < len(data)):
    tokens.append(data[j]['token'])
    j=j+1
    


print(tokens)

now = datetime.now()
 

dt_string = now.strftime("%Y-%m-%d %H:%M:%S")

print("date and time =", dt_string)

msg = "Mensaje de alerta temprana numero 21 prueba"
titulo = "Sistema de Alerta Temprana"
fcm.sendPush(titulo, msg, tokens)






url="http://157.245.254.135/Insert/"



datas = '''
{
    "mensaje" : " '''+ msg +''' ",
    "fecha" : "'''+ dt_string +'''",
    "auxiliar" : "1"
}
'''

_headers = {'Content-Type': 'application/json'}

response = requests.post(url=url,data=datas,headers=_headers)
print(response.content)
url2 = "http://157.245.254.135/auxiliar/1"

datas2 = """
{
    "aux" : 0
    
}
"""

time.sleep( 20 )
response2 = requests.put(url=url2,data=datas2,headers=_headers)
print(response2.content)