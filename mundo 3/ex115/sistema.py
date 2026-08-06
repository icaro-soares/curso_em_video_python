from modulos.interface import *
from time import sleep
from modulos.arquivo import *

arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair'])
    if resp == 1:
        lerArquivo(arq)
    elif resp == 2:
        cabecalho('Cadastro de pessoa...')
    elif resp == 3:
        cabecalho('Saindo...')
        break
    else:
        cabecalho('ERRO! Resposta inválida!')
    sleep(2)
