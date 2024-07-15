# palavra.py
import random


class Palavra:
    def __init__(self, lista_palavra):
        self.palavra = random.choice(lista_palavra)
        self.progresso = ['_' for _ in self.palavra]
        self.letra_adivinhada = set()

    def verificar_letra(self, letra):
        # Converte a letra digitada para minúscula
        letra = letra.lower()

        # Verifica se a letra está na palavra e se não foi adivinhada ainda
        if letra in self.palavra.lower() and letra not in self.letra_adivinhada:
            self.letra_adivinhada.add(letra)
            for i, char in enumerate(self.palavra):
                if char.lower() == letra:  # Comparação case-insensitive
                    self.progresso[i] = self.palavra[i]
            return True
        return False

    def adivinhado(self):
        return '_' not in self.progresso

    def ter_progresso(self):
        return " ".join(self.progresso)
