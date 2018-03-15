from sqlalchemy import create_engine
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import select
from sqlalchemy import MetaData
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import MetaData
# from sqlalchemy.sql import func

engine = create_engine("sqlite:///client.db", echo=True)
metadata = MetaData(engine)

rpc_clients = Table('rpc_client', metadata,
                    Column('codice', String(36), primary_key=True),
                    Column('nome', String(100), nullable=True),
                    Column('cronologia', Integer)
                    )

fatture = Table('fattura', metadata,
                Column('id', Integer, primary_key=True),
                Column('num', String(10), nullable=False),
                Column('ragsoc', String(200), nullable=False)
                )

metadata.create_all(engine)

db = engine.connect()


def get_rpc_client():
    s = select([rpc_clients])
    result = db.execute(s)
    return result.fetchone()


def insert_rpc_client(codice, nome=''):
    ins = rpc_clients.insert().values(codice=codice, nome=nome)
    result = db.execute(ins)
    return result


def insert_fattura(id, num, ragsoc):
    ins = fatture.insert().values(id=id, num=num, ragsoc=ragsoc)
    result = db.execute(ins)
    return result
