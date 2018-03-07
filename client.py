import rpyc, datetime, os, sys, uuid
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import *
from sqlalchemy.sql import func

engine = create_engine("sqlite:///client.db", echo=True)
metadata = MetaData(engine)

rpc_clients = Table('rpc_client', metadata,
	Column('codice', String(36), primary_key=True),
	Column('nome', String(100), nullable=True)
)

metadata.create_all(engine)


# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
#Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
#session = DBSession()

db = engine.connect()

#### Client ####
conn = rpyc.connect("80.211.227.37", 18861)
#c = conn.root.get_cliente(890)
#print c['ragsoc']

#clienti = conn.root.get_clienti()
#for c in clienti:
#    print c['ragsoc']
#print clienti

#fatture = conn.root.get_fatture()
#for f in fatture:
#    print f['ragsoc']

s = select([rpc_clients])
result = db.execute(s)
row = result.fetchone()

if row == None:
    uuid = conn.root.registra_client('aldo', 'password')
    #print uuid
    ins = rpc_clients.insert().values(codice=uuid, nome='Jack Jones')
    result = db.execute(ins)
    #print result
    print 'Registrato nuovo rpc client con codice %s' % uuid
else:
    uuid = row.codice
	
#session.commit()

#codice='6e6779ee-20d5-11e8-9162-00505682af27'
fatture = conn.root.clone(uuid)
print len(fatture)
# for f in fatture:
    # print '%d: %s' %(f['num'], f['ragsoc'])
    
# fatture = conn.root.pull(uuid)
# for f in fatture:
    # print f
    #print '%d: %s' %(f['num'], f['ragsoc'])
