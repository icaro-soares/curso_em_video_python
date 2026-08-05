def arquivo_existe(nome):
    try:
        # Tenta abrir um arquvo
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        # Erro caso não encontre o arquivo
        return False
    else:
        # Caaso encontre o arquivo
        return True


def criar_arquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Algo deu errado na criação do arquivo!')
    else:
        print('Arquivo criado com sucesso!')
