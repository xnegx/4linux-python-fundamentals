#!/usr/bin/python

import psycopg2
from Models.Models import servidores

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


con = psycopg2.connect('host=%s dbname=%s user=%s password=%s' %(
	'localhost','dexter','postgres','123456')
)

cur = con.cursor()

def cadastrar_servidor():
	nome = raw_input('Nome: ')
	ip = raw_input('IP: ')
	administrador = raw_input('Administrador: ')

	servidor = Servidores()
	servidor.nome = nome
	servidor.ip = ip
	servidor.administrador = administrador

	try:
		session.add(servidor)
		session.commit()
		return True
	except Exception as e:
		session.rollback()
		return False




def remover_servidor():
	ip = raw_input('IP: ')
	query = "DELETE FROM servidores WHERE ip = ('%s')" % (ip)
	cur.execute(query)
