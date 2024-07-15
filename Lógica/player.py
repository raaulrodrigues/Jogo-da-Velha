class Player:

    def __init__(self, tentativas_maximas):
        self.tentativas_restante = tentativas_maximas

    # Aqui diminui as tentativas
    def diminuir_tentativas(self):
        self.tentativas_restante -= 1

    # Método para mostrar num de tentativas restantes
    def num_tentativas_restante(self):
        return self.tentativas_restante > 0

    # Método para mostrar num de tentativas atuais
    def num_tentativas_atual(self):
        return self.tentativas_restante
