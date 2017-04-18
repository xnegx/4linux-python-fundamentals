#!usr/bin/python 
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  10 21:21:31 2017
@author: Everton
"""

import os

usuario = "everton"
password = "12345678"

login = raw_input("Digite o seu login de usuario: ")
senha = raw_input("Digite a sua senha: ")

if (login == usuario) and (senha == password):
	os.system('clear')
	print
	print 'Usuario autenticado com sucesso!'
 	print 'Seja Bem Vindo %s' % login
 	print	
else:
	os.system('clear')
	print
 	print 'Acesso Negado!'
 	print