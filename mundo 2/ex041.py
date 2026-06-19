"""Calcula a idade e imprime a categoria que se encaixa"""


from datetime import date


nasc = int(input('Nascimento: '))
idade = date.today().year - nasc
print(f'Sua idade: {idade} anos. Você se encaixa na categoria: ', end='')
if idade <= 9:
    print('Mirim.')
elif idade <= 14:
    print('Infantil.')
elif idade <= 19:
    print('Júnior.')
elif idade <= 25:
    print('Sênior.')
else:
    print('Master.')
