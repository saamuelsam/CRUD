import adiFor
import forca

def jogos():
    print("*********************************")
    print("Escolha o seu jogo!")
    print("*********************************")

    print("(1) Adivinhação (2) Forca")

    int_jogo = int(input("Qual jogo? "))

    if int_jogo == 1:
        print("Jogando Adivinhação")
        adiFor.jogar()
    elif int_jogo == 2:
        print("Jogando Forca")
        forca.jogar()

if (__name__ == "__main__"):
    jogos()