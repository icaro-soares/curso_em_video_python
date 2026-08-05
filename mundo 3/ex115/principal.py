from modulos.interface import *
from modulos.arquivo import *


pessoa = {}
galera = []
arq = 'cursoemvideo.txt'
if not arquivo_existe(arq):
    criar_arquivo(arq)
while True:
    menu()
    opc = int(input('Escolha uma opção: '))
    if opc == 1:
        print('Pessoas cadastradas...')
    elif opc == 2:
        print('-' * 60)
        print('Cadastrando pessoa...')
        pessoa['nome'] = input('Nome: ').strip().title()
        pessoa['idade'] = int(input('Idade: '))
        galera.append(pessoa.copy())
        print('Pessoa cadastrada com sucesso!')
    elif opc == 3:
        print('Saindo...')
        break
    else:
        print('Opção inválida!')
