import random
numero_secreto = random.randint(1, 20)
tentativas = 0
acertou = False
print("Bem-vindo ao jogo de adivinhação!")
print("Estou pensando em um número entre 1 e 20.")

while not acertou:
    palpite = int(input('digite seu palpite: '))
    tentativas += 1
    if palpite < numero_secreto:
        print(f'parabens! voce acertou em {tentativas} tentativas')
    elif palpite > numero_secreto:
        print('muito baixo.... tente novamente')
    else:
        print('muito alto... tente novamente')