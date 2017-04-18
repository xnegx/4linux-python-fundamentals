#!usr/bin/python 
# -*- coding: utf-8 -*-
'''
Created on Wed Apr  11 21:02:01 2017
@author: Everton
'''

from pymongo import MongoClient

client = MongoClient('127.0.0.1')
db = client['devops']


# INSERT
#db.fila.insert({'_id':2,'servico':'intranet','status':0})
#db.fila.insert({'_id':3,'servico':'dns','status':0})

db.fila.find({'usuario':'everton','senha':'12345678'})
# UPDATE
db.fila.update({'_id':3,'servico':'dns'},{'$set':{'status':1}})


# REMOVE
db.fila.remove({'_id':3})

# FIND
for d in db.fila.find({}):
	print d
