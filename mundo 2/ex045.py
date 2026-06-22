"""Jogo de jokenpo"""


from random import randint
from time import sleep


itens = ['Pedra', 'Papel', 'Tesoura']
# escolha do computador e do jogador
computador = randint(0, 2)
jogador = int(input('Sua jogada: [0 - Pedra][1 - Papel][2 - Tesoura] '))
if jogador not in [0, 1, 2]:
    print('Jogada inválida!')
    quit()
else:
    print(f'Você escolheu {itens[jogador]}!')
    print(f'O computador escolheu {itens[computador]}!')
    # condição do jogador ganhar, perder ou empatar
    