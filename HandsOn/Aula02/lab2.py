#!usr/bin/python 
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  10 21:51:31 2017
@author: Everton
"""

import os

usuarios = []

while True:
    print '''
           1 - Cadastrar Usuario
           2 - Acessar Sistema 
           3 - Sair'''

    opcao = input("Digite o numero da opcao desejada: ")

    if opcao == 1:
        usuario = {"login":"","senha":""}
        usuario["login"] = raw_input("Digite o login do usuario: ")
        usuario["senha"] = raw_input("Digite a senha do usuario: ")
        usuarios.append(usuario)

    elif opcao == 2:
        print "-= Sistema de Autenticao =-"
        login = raw_input("Digite o login do usuario: ")
        senha = raw_input("Digite a senha do usuario: ")
        
        for u in usuarios:
            if u["login"] == login and u["senha"] == senha:
                print "Usuario Autenticado com Sucesso"
                break
            else:
                print "Falha ao autenticar"
                break
        else:
            print "Usuario nao encontrado"
    elif opcao == 3:
        print "Saindo do Sistema"
        break




