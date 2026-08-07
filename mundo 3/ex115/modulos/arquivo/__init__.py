from modulos.interface import *


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('\033[31mAlgo deu errado na criação do arquivo!\033[m')
    else:
        print('\033[32mArquivo criado com sucesso!\033[m')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('\033[31mAlgo deu errado!\033[m')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        print(a.read())


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('\033[31mHouve um erro ao abrir o arquivo!\033[m')
    else:
        try:
            a.write(f'{nome:<21}{idade:>21}\n')
        except:
            print('\033[31mHouve um erro no cadastro da pessoa!\033[m')
        else:
            print('\033[32mPessoa cadastrada com sucesso!\033[m')
            a.close()
