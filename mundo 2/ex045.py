"""Jogo de jokenpo"""


from random import randint
from time import sleep


itens = ['pedra', 'papel', 'tesoura']
jogador = int(input('Jogada: [0 - Pedra][1 - Papel][2 - Tesoura] '))
if jogador not in range(0, 3):
    print('Jogada inválida!')
    quit()
computador = randint(0, 2)
print('-=' * 30)
print('JO... ', end='')
sleep(.5)
print('KEN... ', end='')
sleep(.5)
print('PÔ... ')
sleep(.5)
print('-=' * 30)
print(f'Você escolheu {itens[jogador]}')
print(f'Computador escolheu {itens[computador]}')
print('-=' * 30)
if itens[jogador] == 'pedra':
    if itens[computador] == 'pedra':
        print('Deu empate!')
    elif itens[computador] == 'papel':
        print('Você perdeu!')
    elif itens[computador] == 'tesoura':
        print('Você ganhou!')
elif itens[jogador] == 'papel':
    if itens[computador] == 'pedra':
        print('Você ganhou!')
    elif itens[computador] == 'papel':
        print('Deu empate!')
    elif itens[computador] == 'tesoura':
        print('Você perdeu!')
elif itens[jogador] == 'tesoura':
    if itens[computador] == 'pedra':
        print('Você perdeu!')
    elif itens[computador] == 'papel':
        print('Você ganhou!')
    elif itens[computador] == 'tesoura':
        print('Deu empate!')
