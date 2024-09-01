from random import randint

def jogar():
    
    numero_secreto = randint(1, 100)
    tentativa = 0
    pontos = 1000

    print("Bem-vindo ao jogo de adivinhação!")
    print(f"Você tem {pontos} para ganhar!")

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))
    if nivel == 1:
        tentativa = 20
    elif nivel == 2:
        tentativa = 10
    else:
        tentativa = 5

    for rodada in range(1, tentativa + 1):
        chute = input("Digite o seu número: ")
        print(f"Tentativa {rodada} de {tentativa}")
        """print(f"Você tem {} de {} tentativas.".format(tentativa, 3))"""
        print("Você digitou:", chute)

        # Convertendo o chute para inteiro
        chute = int(chute)
        
        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100.")
            continue

        if numero_secreto == chute:
            print(f"Você acertou e fez {pontos} pontos!")
            break
        else:
            if chute > numero_secreto:
                print("Você errou! O seu chute foi maior que o número secreto.")
            elif chute < numero_secreto:
                print("Você errou! O seu chute foi menor que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos

    if rodada == tentativa and chute != numero_secreto:
        print("Você perdeu! O número secreto era", numero_secreto)

if (__name__ == "__main__"):
    jogar()