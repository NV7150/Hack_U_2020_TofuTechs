from websocket import create_connection

import datetime

# pip install websocket-client をすること


def remoteAction():
    t_now = datetime.datetime.now().time()
    ws = create_connection("ws://hacku.australiacentral.cloudapp.azure.com")
    ws.send('{0}:Action occured!'.format(t_now))
    ws.close()