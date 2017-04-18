from Usuarios.usuarios import *

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