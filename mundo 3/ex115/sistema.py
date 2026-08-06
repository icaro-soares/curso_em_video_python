from modulos.interface import *
from time import sleep


while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair'])
    if resp == 1:
        cabecalho('Pessoas cadastradas')
    elif resp == 2:
        cabecalho('Cadastro de pessoa...')
    elif resp == 3:
        cabecalho('Saindo...')
        break
    else:
        cabecalho('ERRO! Resposta inválida!')
    sleep(2)
