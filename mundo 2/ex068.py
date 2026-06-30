from random import randint


computador = randint(0, 10) # alusão a dez dedos das duas mãos
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
    print('Par. Ganhou!') if soma % 2 == 0 else print('Ímpar. Perdeu!')
else:
    print('Ímpar. Ganhou!') if soma % 2 != 0 else print('Par. Perdeu!')
