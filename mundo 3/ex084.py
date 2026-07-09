import os
from time import sleep


lista = []
temp = []
c = 0
while True:
    temp.append(input('Nome: ').strip())
    temp.append(int(input('Peso: ')))
    lista.append(temp[:])
    c += 1
    temp.clear()
    r = ' '
    while r not in 'SsNn':
        r = input('Continuar? [S/N] ')
    if r in 'Nn':
        break
print('-=' * 30)
print(f'Foram cadastradas {len(lista)} pessoas.')