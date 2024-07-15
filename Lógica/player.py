class Player:
    def __init__(self, tentativas_maximas):
        self.tentativas_restante = tentativas_maximas

    def diminuir_tentativas(self):
        self.tentativas_restante -= 1

    def num_tentativas_restante(self):
        return self.tentativas_restante > 0

    def num_tentativas_atual(self):
        return self.tentativas_restante
