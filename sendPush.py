import fcmManager as fcm
import requests
import json
import time
from datetime import datetime

while (True):
    time.sleep(5)
    nombreArchivo = "Alerta_Emergencia.txt"
    nombreSave = "AlertaSave.txt"
    f = open(nombreArchivo, 'r')
    separador = "\n"
    mensaje = f.read()
    msg = mensaje.split(separador)
    url_final = "https://alertaewbs.site/"

    if (msg[0] != ""):

        print(msg[0])
        f.close()

        f = open(nombreArchivo, 'w')
        f.write("")
        f.close()

        f = open(nombreSave, 'w')
        f.write(msg[0])
        f.close()

        url = url_final + "ShowToken/"

        _headers = {'Content-Type': 'application/json'}

        response = requests.get(url=url, headers=_headers)

        data = json.loads(response.text)

        tokens = []
        j = 0
        while (j < len(data)):
            tokens.append(data[j]['token'])
            j = j+1
            print(tokens)
            now = datetime.now()

        dt_string = now.strftime("%Y-%m-%d %H:%M:%S")

        print("date and time =", dt_string)

        msg = msg[0]
        titulo = "Sistema de Alerta Temprana"
        fcm.sendPush(title=titulo, msg=msg, registration_token=tokens)

        url = url_final + "Insert/"

        datas = '''
{
    "mensaje" : " ''' + msg + ''' ",
    "fecha" : "''' + dt_string + '''",
    "auxiliar" : "1"
}
'''

        _headers = {'Content-Type': 'application/json'}

        response = requests.post(url=url, data=datas, headers=_headers)
        print(response.content)
        url2 = url_final + "auxiliar/1"

        datas2 = """
{
    "aux" : 0
    
}
"""

        time.sleep(5)
        response2 = requests.put(url=url2, data=datas2, headers=_headers)
        print(response2.content)

    else:
        print("vacio")
