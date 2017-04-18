#!usr/bin/python 
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 19:48:25 2017
@author: Everton
"""
import datetime 
import time

#print datetime.now()

print "A data atual e: " , datetime.datetime.now()
print "A data em segundos: %s" %time.time()
print "Ou assim ?: ", datetime.datetime.now().strftime("%d/%b/%Y")
print "Ano atual: ", datetime.date.today().strftime("%Y")
print "Mes atual: ", datetime.date.today().strftime("%B")
print "Numero da semana do ano: ", datetime.date.today().strftime("%W")
print "Dia da semana: ", datetime.date.today().strftime("%w")
print "Dia do anao: ", datetime.date.today().strftime("%j")
print "Dia do mes: ", datetime.date.today().strftime("%d")
print "Dia da semana: ", datetime.date.today().strftime("%A")