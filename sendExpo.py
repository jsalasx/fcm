import fcmManager as fcm
import expoManager as expoManager
import sendApple as appleFcm
import requests
import json
import time
from datetime import datetime

# pip install exponent_server_sdk

while (True):

    nombreArchivo = "Alerta_Emergencia.txt"
    nombreSave = "AlertaSave.txt"
    f = open(nombreArchivo, 'r')
    separador = "\n"
    mensaje = f.read()
    msg = mensaje.split(separador)
    url_final = "https://alertaewbs.site/"
    # url_final = "http://localhost:8000/"
    if (msg[0] != ""):

        print(msg[0])
        f.close()

        f = open(nombreArchivo, 'w')
        f.write("")
        f.close()

        f = open(nombreSave, 'w')
        f.write(msg[0])
        f.close()

        msg = msg[0]  # mensaje

        endPoint = url_final + "api/token/"
        dataAuth = {"email": "joal.sala@gmail.com",
                    "password": "Ximesamy2020.",
                    "username": "xtdrack"}
        _headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(url=endPoint, headers=_headers, data=dataAuth)
        dataToken = json.loads(response.text)

        url = url_final + "ShowToken/"  # consulta tokens
        tokenAuth = dataToken["access"]
        # print(tokenAuth)
        bearerToken = 'Bearer ' + tokenAuth
        _headers = {'Content-Type': 'application/json',
                    'Authorization': bearerToken}
        response = requests.get(url=url, headers=_headers)
        data = json.loads(response.text)
        # print(data)
        # guardar mensajes
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
        #print("date and time =", dt_string)

        url = url_final + "Insert/"

        datas = '''
            {
                "mensaje" : " ''' + msg + ''' ",
                "fecha" : "''' + dt_string + '''",
                "auxiliar" : "1"
            }
            '''
        _headers = {'Content-Type': 'application/json',
                    'Authorization': bearerToken}
        response = requests.post(url=url, data=datas, headers=_headers)

        j = 0
        titulo = "Sistema de Alerta Temprana"
        tokens = []
        while (j < len(data)):
            tokenApple = appleFcm.getToken()
            deviceId = data[j]['token']
            esAndroid = data[j]['esAndroid']
            if (esAndroid == '1'):
                tokens.append(data[j]['token'])
            else:
                appleFcm.sendMessageIphone(tokenApple, deviceId, msg)
            #expoManager.send_push_message(data[j]['token'], msg)
            j = j+1

        # print(titulo)
        # print(msg)
        fcm.sendPush(title=titulo, msg=msg, registration_token=tokens)
        time.sleep(10)
    else:
        print("vacio")
        time.sleep(3)
