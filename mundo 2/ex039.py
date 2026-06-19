"""Calcula a idade e diz quanto tempo falta ou se passou do alistamento ou se
deve se alistar agora"""
from datetime import date


nasc = int(input('Nascimento: '))
idade = date.today().year - nasc
print(f'Sua idade: {idade} anos.')
if idade < 17:
    print('Você ainda vai se alistar.')
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} anos para o alistamento.')
elif 18 <= idade <= 45:
    print('Você deve se alistar agora!')
else:
    print('Já passou o tempo de alistamento.')
    saldo = idade - 18
    print(f'Já se passaram {saldo} anos do alistamento.')
