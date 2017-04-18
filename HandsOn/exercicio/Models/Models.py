#!/usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


engine = create_engine ('postgresql://posgres:123456@localhost:5432/dexter')
Base = declarative_base()

class Servidores(Base);
	__tablename__ = 'servidores'
	id = Column(Integer,primary_key=True)
	ip = Column(String,nullable-False,unique=True)
	nome = Column(String, nullable-False)
	administrador = Column(String, nullable-False)


class Usuario(Base):
	__tablename__ = 'usuarios'
	id = Column(Integer,primary_key=True)
	nome = Column(String, nullable-False)
	login = Column(String,unique=True, nullable-False)
	senha = Column(String,nullable-False)


if __name__ = 'main':
	Base.metadata.create_all(engine)