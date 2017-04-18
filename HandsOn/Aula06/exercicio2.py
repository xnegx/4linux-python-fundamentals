#!usr/bin/python 
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 21:27:31 2017
@author: Everton
"""

import psycopg2
import os
con = psycopg2.connect('host=%s dbname=%s user=%s password=%s' %(
	'localhost','projeto','postgres','123456'
	)
)

cur = con.cursor()
session = False
flag = True
while flag:

	banner = '''Menu:
1) Logar
2) Cadastrar usuario
3) Listar usuario
4) Sair

Selecione a opcao: '''

	option = int(raw_input(banner))
	if option == 1:
		print 'Opcao 1 selecionada - Login'
		usuario = raw_input('Username: ')
		senha = raw_input('Password: ')
		query = "SELECT * FROM users WHERE usuario='%s' AND pass='%s'" % (usuario, senha)
		cur.execute(query)
		usuario = cur.fetchone()
		if usuario:
			session = True
			print
			os.system('clear')
			print 'Logado com sucesso!'
			print
		else:
			os.system('clear')
			print 'Username ou password invalidos'	

	elif option == 2:
		print
		os.system('clear')
		print 'Opcao 2 selecionada - Cadastrar usuario'
		if session == True:
			usuario = raw_input('Digite o usuario que deseja incluir: ')
			senha = raw_input('Digite a senha para o usuario: ')
			query = "INSERT INTO users (usuario,pass) VALUES ('%s', '%s')" % (usuario,senha)
			cur.execute(query)
			try:
				if cur.rowcount:
					print 'Registro inserido com sucesso!'
					con.commit()
			except Exception as e:
				print e
				con.rollback()
		else:
			os.system('clear')
			print '*****ERRO***** !'
			print 'Voce nao esta logado, realize o login primeiro'
		print
	elif option == 3:
		print
		os.system('clear')
		print 'Opcao 3 selecionada - Procurar usuario'
		if session == True:
			usuario = raw_input('Digite o usuario que deseja buscar: ')
			query = "SELECT * FROM users WHERE usuario LIKE '%%%s%%'" % (usuario)
			cur.execute(query)
			usuario = cur.fetchone()
			if usuario != None:
				os.system('clear')
				print '*****RESULTADO DA BUSCA*****:'
				print
				print 'Usuario: %s\nSenha: %s' %(usuario[1],usuario[2])
			else:
				print
				print 'Erro !, usuario nao encontrado'
		else:
			print '*****ERRO***** !'
			print 'Voce nao esta logado, realize o login primeiro'
		print
	elif option == 4:
		print
		print 'Volte sempre'
		print
		flag = False