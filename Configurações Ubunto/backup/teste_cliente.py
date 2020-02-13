import unittest
from should_dsl import should
from cliente import Cliente

class TesteCliente(unittest.TestCase):

     def setUp(self):
        self.um_cliente = Cliente('Juca', 12345678910)

     def testeCompra(self):
         self.um_cliente.compra(0)
         self.um_cliente.comprou |should| be(False)
         self.um_cliente.compra(1)
         self.um_cliente.comprou |should| be(True)
         self.um_cliente.compra(2)
         self.um_cliente.comprou |should| be(True)

if __name__ == '__main__':
    unittest.main()
         


