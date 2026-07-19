import os
from time import sleep


dados = {}
ficha = []
soma_idade = 0
while True:
    dados['nome'] = input('Nome: ').strip().title()
    dados['sexo'] = ' '
    while dados['sexo'] not in 'MmFf':
        dados['sexo'] = input('Sexo: [M/F] ').strip()[0]
    dados['idade'] = int(input('Idade: '))
    soma_idade += dados['idade']
    ficha.append(dados.copy())
    r = ' '
    while r not in 'SsNn':
        r = input('Continuar: [S/N] ').strip()[0]
    if r in 'Nn':
        break
print('Analisando... ')
sleep(2)
os.system('cls' if os.name == 'nt' else 'clear' )
print('-=' * 30)
print(f'Pessoas cadastradas: {len(ficha)}')
média_idade = soma_idade / len(ficha)
print(f'Média de idade do grupo: {média_idade:.1f}')
print('Lista de mulheres:')
for p in ficha:
    if p['sexo'] in 'Ff':
        print(f'\t=> {p['nome']}')
print('Pessoas acima da média de idade:')
for p in ficha:
    if p['idade'] > média_idade:
        print(f'\t{p['nome']}; {p['sexo']}; {p['idade']}')
