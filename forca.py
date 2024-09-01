import random

def jogar():
    msg_abertura()
    secret_word = update_secret_word()
    world = inicializa_letras_acertadas(secret_word) 
    letras_chutadas = []
    
    enforce = False
    correct = False
    error = 0
    
    while(not enforce and not correct): # Enquanto não for enforcado e não for correto
        desenhar_enforcado(error) # Desenha o enforcado de acordo com o número de erros
        chute = pede_chute(world, letras_chutadas) # Pede um chute

        if chute in letras_chutadas:
            print("Você já chutou essa letra. Tente outra.")
            continue

        letras_chutadas.append(chute)
        
        if(chute in secret_word): # Verifica se a letra está na palavra
            marca_chute_correto(chute, secret_word, world)
        else:
            error += 1
        if(error == 7):
            enforce = check_game_over() # Verifica se o jogo acabou

        correct = "_" not in world # Verifica se todas as letras foram acertadas
        print(world)
    
    if(correct):
        imprimir_mensagem_vencedor()
    else:
        desenhar_enforcado(error) # Desenha a última parte do enforcado
        imprime_mensagem_perdedor(secret_word)

def desenhar_enforcado(erros):
    estagios = [
        """
        +---+
        |   |
            |
            |
            |
            |
        =========""",
        """
        +---+
        |   |
        O   |
            |
            |
            |
        =========""",
        """
        +---+
        |   |
        O   |
        |   |
            |
            |
        =========""",
        """
        +---+
        |   |
        O   |
       /|   |
            |
            |
        =========""",
        """
        +---+
        |   |
        O   |
       /|\\  |
            |
            |
        =========""",
        """
        +---+
        |   |
        O   |
       /|\\  |
       /    |
            |
        =========""",
        """
        +---+
        |   |
        O   |
       /|\\  |
       / \\  |
            |
        ========="""
    ]
    if erros < len(estagios):
        print(estagios[erros])

def imprime_mensagem_perdedor(secret_word):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(secret_word))
    desenhar_caveira()

def imprimir_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("                         ")
    print("       ___________       ")
    print("      '._==_==_=_.'      ")
    print("      .-\|:      /-.     ")
    print("     | (|:.     |) |     ")
    print("      '-|:.     |-'      ")
    print("        \|::.    /       ")
    print("         '::. .'         ")
    print("           ) (           ")
    print("         _.' '._         ")
    print("        '-------'        ")

def check_game_over():
    return True

def marca_chute_correto(chute, secret_word, world):
    index = 0 
    for letter in secret_word: # Percorre a palavra secreta
        if(chute == letter): # Verifica se a letra é igual a letra da palavra
            world[index] = chute
        index += 1

def pede_chute(world, letras_chutadas):
    chute = input("Qual a letra? {}. Letras chutadas: {}".format(world, letras_chutadas)) # Pede uma letra
    chute = chute.strip().lower() # Remove espaços e coloca em minúsculo
    return chute

def msg_abertura():
    print("*********************************")
    print("Bem-vindo ao jogo de Forca!")
    print("*********************************")
    
def update_secret_word():
    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        palavras.append(linha.strip())
    arquivo.close()

    numero = random.randrange(0, len(palavras)) # Gera um número aleatório
    secret_word = palavras[numero].lower()
    return secret_word 

# Pega a palavra secreta
def inicializa_letras_acertadas(secret_word):
    return ["_" for letra in secret_word] # Cria uma lista com o tamanho da palavra secreta

def desenhar_caveira():
    caveira = """
       _____
     /     \\
    | () () |
     \  ^  /
      |||||
      |||||
    """
    print(caveira)

if (__name__ == "__main__"):
    jogar()
