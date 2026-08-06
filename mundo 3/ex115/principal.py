from modulos.interface import *
from time import sleep


while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa',
                 'Sair'])
    if resp == 1:
        cabecalho('Pessoas cadastradas...')
    elif resp == 2:
        cabecalho('Cadastrar nova pessoa...')
    elif resp == 3:
        cabecalho('Saindo...')
        break
    else:
        cabecalho('Opção inválida!')
    sleep(2)
