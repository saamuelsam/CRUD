print("tudo bem como")

numero_secreto = 42

chute = input("Digite o seu número: ")

print("Você digitou: ", chute)

"""chute = int(chute)"""

if (numero_secreto == int(chute)):
    print("Você acertou!")
else:
    if(int(chute) > numero_secreto):
        print("Você errou! O seu chute foi maior que o número secreto.")
    elif(int(chute) < numero_secreto):
        print("Você errou! O seu chute foi menor que o número secreto.")
    
print("Fim do jogo!")
