#!/usr/bin/python

import psycopg2

con = psycopg2.connect('host=%s dbname=%s user=%s password=%s' %(
	'localhost','dexter','postgres','123456')
)

cur = con.cursor()

def cadastrar_servidor():
	nome = raw_input('Nome: ')
	ip = raw_input('IP: ')
	administrador = raw_input('Administrador: ')
	query = "INSERT INTO servidores (nome,ip,administrador) VALUES ('%s', '%s','%s')" % (nome,ip,administrador)
	cur.execute(query)

	try:
		if cur.rowcount:
			con.commit()
			return True
	except Exception as e:
		print e
		con.rollback()
	return False


def remover_servidor():
