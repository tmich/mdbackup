import rpyc, datetime, os, sys, uuid
import database as db

HOST = "80.211.227.37"
PORT = 18861

class RpcClient:

	def __init__(self):
		self.server = None
		self.async_fatt = None
		# client = db.get_rpc_client()

		# if client == None:
			# registra_client()
		# else:
			# uuid = client.codice
			
	def connect(self):
		self.server = rpyc.connect(HOST, PORT)
			
	def login(self, username, password):
		#uuid = server.root.registra_client('aldo', 'password')
		print('%s, %s' % (username, password))
		i = self.server.root.login(username, password)
		#print(i)
		return i

	def registra_client(self):
		uuid = self.server.root.registra_client('aldo', 'password')
		if db.insert_rpc_client(uuid, 'tiziano'):
			print('Registrato nuovo rpc client con codice %s' % uuid)
		else:
			raise exception('non valido')
			
	def aggiorna_async(self):
		print 'aggiorna_async'
		self.async_fatt = rpyc.async(self.server.root.get_fatture)
		self.async_result = self.async_fatt()
		return self.async_result
	
	#def aggiornamento_callback(self):	
		
	
		
	#session.commit()

	#codice='6e6779ee-20d5-11e8-9162-00505682af27'
	# fatture = server.root.clone(uuid)
	# print fatture
	# for f in fatture:
		# print '%d: %s' %(f['num'], f['ragsoc'])
		
	# fatture = server.root.pull(uuid)
	# for f in fatture:
		# print f
		#print '%d: %s' %(f['num'], f['ragsoc'])