class Cliente:

    def __init__(self, nome, cpf):
          self.nome = nome
          self.cpf = cpf

    def compra (self, codigo_produto):
            if codigo_produto == 0:
              produto = 'Produto nenhum'
              self.comprou = False
            elif codigo_produto == 1:
              produto = 'CD'
              self.comprou = True
            else codigo_produto == 2:
              produto = 'DVD'
              self.comprou = True

              return produto
               
