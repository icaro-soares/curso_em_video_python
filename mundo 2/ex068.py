from random import randint


computador = randint(0, 10) # alusão a dez dedos das duas mãos
jogador = ' '
while jogador not in range(0, 11):
    jogador = int(input('Escolha um número: [entre 0 e 10] '))
    if jogador not in range(0, 11):
        print('Válido apenas número de dedos!')
