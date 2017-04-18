#!usr/bin/python 
# -*- coding: utf-8 -*-
'''
Created on Wed Apr  12 19:22:01 2017
@author: Everton
'''

import psycopg2

class Conexao:


	@staticmethod
	def conecta(host,db,user,passwd):
		con = psycopg2.connect('host=%s dbname=%s user=%s password=%s' % (host,db,user,passwd))
		cur = con.cursor()
		return con,cur


class Banco:
	con = None
	cur = None

	def __init__(self,host,db,user,passwd):
		self.con,self.cur = Conexao.conecta(host,db,user,passwd)


	def find_one(self,id):
		self.cur.execute ("SELECT * FROM post WHERE id= %s" % id)
		return self.cur.fetchone()


	def find_all(self,):
		self.cur.execute ("SELECT * FROM post")
		return self.cur.fetchall()


	def incluir(self,titulo,conteudo):
		self.cur.execute("INSERT INTO post(titulo,conteudo) VALUES ('%s','%s')"  %(titulo,conteudo))
		self.con.commit()


	def update(self,titulo,conteudo):
		pass


objeto = Banco('localhost','projeto','postgres','123456')

print objeto
print
print objeto.find_one(1)


objeto.incluir('titulo de classe','conteudo de classe')

print
for row in objeto.find_all():
	print 'ID: %s \nTitulo: %s\n Conteudo: %s' % (row)
print
