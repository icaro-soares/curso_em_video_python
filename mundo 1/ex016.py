"""Calcula a parte inteira de um valor float"""


from math import trunc


num = float(input('Digite um número real: '))
print(f'A parte inteira de {num} é {trunc(num)}')
