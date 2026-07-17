import os
from datetime import date
# aposentadoria por anos contribuição 35 anos H e M
from time import sleep

ficha = {}
ficha['nome'] = input('Nome do trabalhador: ').strip().title()
atual = date.today().year
ficha['nasc'] = int(input('Nascimento [0 p/ ano atual] '))
if ficha['nasc'] == 0:
    ficha['nasc'] = atual
    quit()
elif ficha['nasc'] < 0 or ficha['nasc'] > atual:
    print('Ano inválido!')
    quit()
ficha['idade'] = atual - ficha['nasc']
ficha['ctps'] = int(input('Digite a ctps: [0 não tem] '))
if ficha['ctps'] != 0:
    ficha['contratação'] = int(input('Ano de contratação: '))
    ficha['tempo_empregado'] = atual - ficha['contratação']
    ficha['salário'] = float(input('Salário: R$'))
print('Analisando...')
sleep(2)
os.system('cls') if os.name == 'nt' else os.system('clear')
for k, v in ficha.items():
    print(f'O campo {k} tem valor {v}')
print('-=' * 30)
if ficha['ctps'] != 0:
    ficha['contribuição'] = 35 - ficha['tempo_empregado']
    print(f'Faltam {ficha['contribuição']} anos para se aposentar.')
else:
    print('O trabalhador não possui ctps')
