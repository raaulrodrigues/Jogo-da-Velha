from Lógica.palavra import Palavra
from Lógica.player import Player


class Forca:
    def __init__(self, lista_palavras, tentativas_maximas):
        self.player = Player(tentativas_maximas)
        self.palavra = Palavra(lista_palavras)

    def start(self):
        print("!! Jogo da Forca !!")
        while self.player.num_tentativas_restante() and not self.palavra.adivinhado():
            print("Palavra: ", self.palavra.ter_progresso())
            print("\nChances restante: ", self.player.tentativas_restante)
            chute = input("Chute uma letra: ").lower()

            if self.palavra.verificar_letra(chute):
                print("\nEssa letra está correta!")
            else:
                print("\nEssa letra está errada!")
                self.player.diminuir_tentativas()

        if self.palavra.adivinhado():
            print("Você adivinhou a palavra: ", self.palavra.palavra)
        else:
            print("Você perdeu, mas a palavra era: ", self.palavra.palavra)
