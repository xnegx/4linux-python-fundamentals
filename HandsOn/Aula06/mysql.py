#!usr/bin/python 
# -*- coding: utf-8 -*-
'''
Created on Wed Apr  11 19:14:31 2017
@author: Everton
'''

import MySQLdb

con = MySQLdb.connect(host='127.0.0.1', user='admin',passwd='b2-4ac2a',db='projeto')

cur = con.cursor()

# INSERT

try:
	cur.execute("INSERT INTO posts(titulo,conteudo) VALUES ('Meu Titulo','Meu conteudo')")
	con.commit()
except Exception as e:
	con.rollback()

# UPDATE

try:
	cur.execute("UPDATE posts SET titulo='Novo Titulo' WHERE id = 1")
	con.commit()
except Exception as e:
	con.rollback()

# SELECT ONE

cur.execute ("SELECT * FROM posts WHERE id =1")
print
print '1 RESULTADO' 
print cur.fetchone()
print


# SELECT ALL
cur.execute ("SELECT * FROM posts")
print 'TODOS RESULTADOS'
for row in cur.fetchall():
	print row
print

con.close