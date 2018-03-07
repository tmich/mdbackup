import rpyc, datetime, os, sys, uuid
import database as db

class RpcClient:

	def __init__(self):
		self.server = rpyc.connect("80.211.227.37", 18861)
		
		# client = db.get_rpc_client()

		# if client == None:
			# registra_client()
		# else:
			# uuid = client.codice
			
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