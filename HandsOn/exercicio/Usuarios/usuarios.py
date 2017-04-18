#!/usr/bin/python

import psycopg2

con = psycopg2.connect('host=%s dbname=%s user=%s password=%s' %(
	'localhost','dexter','postgres','123456')
)

cur = con.cursor()




def cadastrar_usuario(): 
	nome = raw_input('Nome: ')
	login = raw_input('Login: ')
	senha = raw_input('Senha: ')
	query = "INSERT INTO usuarios (nome,login,senha) VALUES ('%s', '%s','%s')" % (nome,login,senha)
	cur.execute(query)

	try:
		if cur.rowcount:
			con.commit()
			return True
	except Exception as e:
		print e
		con.rollback()
	return False


def logar():
	login = raw_input('Login: ')
	senha = raw_input('Senha: ')
	query = "SELECT * FROM usuarios WHERE login='%s' AND senha='%s'" % (login, senha)
	cur.execute(query)
	login = cur.fetchone()
	if login:
		print
		return True
		print
	else:
		return False
