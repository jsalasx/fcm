import firebase_admin
from firebase_admin import credentials, messaging

cred = credentials.Certificate(
    "./alertaewbsuno-firebase-adminsdk-r7ln0-5c33e8a9dd.json")
firebase_admin.initialize_app(cred)


def sendPush(title, msg, registration_token, dataObject=None):
    # See documentation on defining a message payload.
    message = messaging.MulticastMessage(
        notification=messaging.Notification(
            title=title,
            body=msg
        ),
        data=dataObject,
        tokens=registration_token,
    )

    # Send a message to the device corresponding to the provided
    # registration token.
    response = messaging.send_multicast(message)
    # Response is a message ID string.
    print('Successfully sent message:', response)


def send_to_token_multicast(self, registration_tokens, title, body, data=None):
    # registration_tokens has to be a list
    assert isinstance(registration_tokens, list)

    message = messaging.MulticastMessage(
        notification=messaging.Notification(
            title=title,
            body=body,
        ),
        data=data,
        token=registration_tokens
    )
    response = messaging.send_multicast(message)
    print(response)
    # See the BatchResponse reference documentation
    # for the contents of response.
    return response
