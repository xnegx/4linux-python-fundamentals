#!usr/bin/python 
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 21:23:31 2017
@author: Everton
"""

import psycopg2

con = psycopg2.connect('host=%s dbname=%s user=%s password=%s' %(
	'localhost','projeto','postgres','123456'
	)
)
# ------------- INSERT UPDATE DELETE

try:
	cur = con.cursor()
	cur.execute("INSERT INTO post(conteudo,titulo) VALUES ('A crise no Brasil', 'Bla bla bla')")

	if cur.rowcount:
		print 'Registro inserido com sucesso!'
		con.commit()
except Exception as e:
	print e
	con.rollback()
