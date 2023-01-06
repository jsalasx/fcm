import jwt
import time
import json

from hyper import HTTPConnection
ALGORITHM = 'ES256'

APNS_KEY_ID = '6JHT6RS3T3'
APNS_AUTH_KEY = 'AuthKey_6JHT6RS3T3.p8'
TEAM_ID = 'UFB9P7DZX3'
BUNDLE_ID = 'com.xtdrack.alertap'


def sendMessageIphone(token, deviceId, msg):
    REGISTRATION_ID = deviceId
    path = "/3/device/" + format(REGISTRATION_ID)

    request_headers = {

        'apns-expiration': '0',
        'apns-priority': '10',
        'apns-push-type': 'alert',
        'apns-topic': BUNDLE_ID,
        'authorization': 'bearer ' + token
    }
    payload_data = {
        'aps': {
            'alert': {
                "title": "Sistema de Alerta Temprana",
                "body": msg
            }
        }
    }
    payload = json.dumps(payload_data).encode('utf-8')
    conn = HTTPConnection('api.push.apple.com:443')
    conn.request(
        'POST',
        path,
        payload,
        headers=request_headers
    )
    resp = conn.get_response()
    # print("hola")
    # print(resp.status)
    # print(resp.read())


def getToken():
    f = open(APNS_AUTH_KEY)
    secret = f.read()
    token = jwt.encode(
        {
            'iss': TEAM_ID,
            'iat': time.time()
        },
        secret,
        algorithm=ALGORITHM,
        headers={
            'alg': ALGORITHM,
            'kid': APNS_KEY_ID,
        }
    )
    return token


#token = getToken()
# sendMessageIphone(token)
# print(token)
