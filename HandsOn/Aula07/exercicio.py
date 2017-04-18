#!usr/bin/python 
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# SQLITE3
engine = create_engine ('sqlite:///banco.db')

#POSTGRE
# engine = create_engine ('postgresql://posgres:123456@localhost:5432/projeto')

# MYSQL
#engine = create_engine('mysql://admin:b2-4ac2a@localhost/projeto')




Base = declarative_base()


class Usuario(Base):
	__tablename__ = 'usuarios'
	id = Column(Integer, primary_key=True)
	nome = Column(String)


if __name__ == '__main__':
	Base.metadata.create_all(engine)
	Session = sessionmaker()
	Session.configure(bind=engine)
	session = Session()


	lista = ['everton','joao','silva']
	# print lista

	for l in lista:
		usuario = Usuario(nome = l)
		session.add(usuario)
		session.commit()

	for i in session.query(Usuario).all():
		print 'Usuario %s com ID: %s adicionado com sucesso' % (i.nome, i.id)

