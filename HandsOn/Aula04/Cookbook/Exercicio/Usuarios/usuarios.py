#!/usr/bin/python

usuarios = []
senhas = []

def cadastrar_usuario(): 
	global usuarios,senhas
	login = raw_input('Login: ')
	senha = raw_input('Senha: ')
	usuarios.append(login)
	senhas.append(senha)

	return True


def logar():
	global senhas,usuarios
	login = raw_input('Insira o login: ')
	senha = raw_input('Insira a senha: ')

	if login in usuarios:
		if senhas[usuarios.index(login)] == senha:
			return True
	return False