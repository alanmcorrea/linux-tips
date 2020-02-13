class Pessoa:
    def __init__(self, posicao):
        self.posicao = posicao

    def andar(self,distancia):
        self.posicao = self.posicao + distancia

    def comer(self, rango):
        if rango == 'alface':
            self.esta_satisfeita = False
        elif rango == 'picanha':
            self.esta_satisfeita = True
        else:
            self.esta_satisfeita = False
