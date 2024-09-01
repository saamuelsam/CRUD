print("Bem-vindo ao jogo de adivinhação!")

numero_secreto = 42
tentativa = 3
rodada = 1

while tentativa > 0: # Enquanto o número de tentativas for maior que 0
    chute = input("Digite o seu número: ")
    print(f"Tentativa {rodada} de 3")
    """print(f"Você tem {} de {} tentativas.".format(tentativa, 3))"""
    print("Você digitou:", chute)

    # Convertendo o chute para inteiro
    chute = int(chute)

    if numero_secreto == chute:
        print("Você acertou!")
        break
    else:
        if chute > numero_secreto:
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif chute < numero_secreto:
            print("Você errou! O seu chute foi menor que o número secreto.")
        
    rodada += 1 # Incrementando o número da rodada
    tentativa -= 1 # Decrementando o número de tentativas

    if tentativa == 0:
        print("Você perdeu! O número secreto era", numero_secreto)