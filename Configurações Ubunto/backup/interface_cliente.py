from cliente import Cliente

class InterfaceCliente:

  Cliente.nome = input("Digite o seu nome: ")
  Cliente.cpf = input("Digite o seu cpf: ")

  codpro = input("Escolha o produto: \n\n(1) - CD \n\n(2) - DVD \n\n(0) - Nao Comprar\n\n  ->")

Cliente.compra(codpro)

print '\n'

print '%s, voce escolheu : %s !!!' % (Cliente.nome, Cliente.produto)

