from Usuarios.usuarios import *

while True:
  print '''
           1 - Cadastrar Usuario
           2 - Acessar Sistema
           3 - Cadastrar Servidor
           4 - Excluir Servidor 
           0 - Sair
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
    if cadastrar_servidor():
      print 'Servidor cadastrado com sucesso'
    else:
      print 'Falha ao cadastrar servidor'
  elif opcao == 4:
    if remover_servidor():
      print 'Servidor removido com sucesso'
    else:
      print 'Falha ao remover servidor'
  elif opcao == 0:
    print "Saindo do Sistema"
    break