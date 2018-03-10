import rpyc
# import datetime
# import os
# import sys
# import uuid
import database as db

HOST = "80.211.227.37"
PORT = 18861


class RpcClient:

    def __init__(self):
        self.server = None
        self.async_fatt = None

    def connect(self):
        self.server = rpyc.connect(HOST, PORT)
        print 'Connessione in corso...'

    def login(self, username, password):
        print('%s, %s' % (username, password))
        i = self.server.root.login(username, password)
        return i

    def registra_client(self):
        uid = self.server.root.registra_client('aldo', 'password')
        if db.insert_rpc_client(uid, 'tiziano'):
            print('Registrato nuovo rpc client con codice %s' % uid)
        else:
            raise Exception('non valido')

    def aggiorna_async(self):
        print 'aggiorna_async'
        self.async_fatt = rpyc.async(self.server.root.clone)
        self.async_result = self.async_fatt()
        return self.async_result
