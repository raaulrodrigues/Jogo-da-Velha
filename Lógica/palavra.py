import random


class Palavra:

    def __init__(self, lita_palavra):
        self.palavra = random.choice(lita_palavra)
        self.progresso = ['_' for _ in self.palavra]
        self.letra_adivinhada = set()

    def verificar_letra(self, letra):
        # Verificamos se a letra está na palavra e se não foi adivinhada ainda
        if letra in self.palavra and letra not in self.letra_adivinhada:
            # Adiciona ao letra_adivinhada caso tenha sido acertada
            self.letra_adivinhada.add(letra)
            # Para fazer cada letra 'virar um int' para retornar um índice e a letra
            for i, char in enumerate(self.palavra):
                if char == letra:
                    # Atualizamos a posição com a letra correta
                    self.progresso[i] = letra
            return True
        return False

    # Métodos para verificar se teve progresso e se caso tenha, mostrar ele
    def adivinhado(self):
        return '_' not in self.progresso

    def ter_progresso(self):
        return " ".join(self.progresso)
