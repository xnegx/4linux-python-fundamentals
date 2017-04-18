#!usr/bin/python 
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 20:00:31 2017
@author: Everton
"""


# --- CONEXAO COM O BANCO
import psycopg2

con = psycopg2.connect('host=%s dbname=%s user=%s password=%s' %(
	'localhost','projeto','postgres','123456'
	)
)

print '1 = Para Inserir registro no banco'
print '2 = Para buscar um post no banco'
opcao = input('Escolha uma opçao: ')

if opcao == 1:
	print 'Opcao 1 selecionada'
	titulo = raw_input('Digite o titulo: ')
	conteudo = raw_input('Digite o conteudo: ')
	try:
		cur = con.cursor()
		cur.execute("INSERT INTO post(conteudo,titulo) VALUES ('%s', '%s')" % (titulo,conteudo))

		if cur.rowcount:
			print 'Registro inserido com sucesso!'
			con.commit()
	except Exception as e:
		print e
		con.rollback()

else:
	print 'Opcao 2 selecionada'
	conteudo = raw_input('Digite o conteudo a ser buscado: ')
	print
	print 'Resultado da busca:'
	print
	cur = con.cursor()
	cur.execute("SELECT * FROM post WHERE conteudo LIKE ('%s')" % (conteudo))
	for row in cur.fetchall():
		print 'ID: %s \nTitulo: %s\nConteudo: %s' % (row)
		print
