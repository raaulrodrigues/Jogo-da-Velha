from Lógica.forca import Forca
from Principal.lista_palavras import temas


def main():
    print("Temas para jogar: \n"
          "[1] Animais\n"
          "[2] Frutas\n"
          "[3] Países\n")

    escolha = int(input("Escolha um dos temas: "))
    tema = list(temas.keys())[escolha - 1]

    jogo = Forca(temas[tema], 10)
    jogo.start()


if __name__ == "__main__":
    main()
