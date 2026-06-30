from random import randint

vitorias = 0

while True:
    computador = randint(0, 10) # computador sorteia um número de 0 a 10

    jogador = ' '
    while jogador not in range(0, 11):
        jogador = int(input('Escolha um número: [entre 0 e 10] '))
        if jogador not in range(0, 11):
            print('Válido apenas número de dedos!')

    soma = jogador + computador

    opc = ' '
    while opc not in 'PpIi':
        opc = input('Par ou Ímpar: [P/I] ').strip()[0]
        if opc not in 'PpIi':
            print('Escolha inválida, escolha novamente!')
    print(f'Você jogou {jogador} e o computador {computador}.')
    if opc in 'Pp':
        if soma % 2 == 0:
            print('Par. Ganhou!')
            vitorias += 1
        else:
            print('Ímpar. Perdeu!')
            break
    else:
        if soma % 2 != 0:
            print('Ímpar. Ganhou!')
            vitorias += 1
        else:
            print('Par. Perdeu!')
            break
print('-=' * 30)
print(f'Game over! Total de vitórias: {vitorias}.')
