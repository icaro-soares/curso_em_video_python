from random import randint


computador = randint(0, 9) # alusão a dez dedos das duas mãos
jogador = int(input('Digite um valor: [0 e 9] '))
if jogador not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print('Válido apenas número de dedos!')
    quit()
print(computador)
