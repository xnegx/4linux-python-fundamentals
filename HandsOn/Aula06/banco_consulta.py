#!usr/bin/python 
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 21:23:31 2017
@author: Everton
"""

import psycopg2

con = psycopg2.connect('host=%s dbname=%s user=%s password=%s' %(
	'localhost','projeto','postgres','123456'
	)
)

# ------------- SELECT
cur = con.cursor()
cur.execute("SELECT * FROM post")

#print cur.fetchall()

for row in cur.fetchall():
	print 'ID: %s \nTitulo: %s\n Conteudo: %s' % (row)