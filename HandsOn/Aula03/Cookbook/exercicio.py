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

while True:
    print '''
           1 - Cadastrar Usuario
           2 - Acessar Sistema 
           3 - Sair
           '''

    opcao = input("Digite o numero da opcao desejada: ")

    if opcao == 1:
    	if cadastrar_usuario():
    		print 'Usuario cadastrado com sucesso'
    	else:
    		print 'Falha ao cadastrar'
    elif opcao == 2:
    	if logar():
    		print 'Login realizado com sucesso!'
    	else:
    		print 'Login ou senha invalidos'
     
    elif opcao == 3:
        print "Saindo do Sistema"
        break

