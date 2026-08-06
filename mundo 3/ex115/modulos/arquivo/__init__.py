def abrirArquivo(nome):
    try:
        # Tentativa de abri o arquivo
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        # Tentativa falha
        return False
    else:
        # Tentativa com sucesso
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        return False
    else:
        print('Arquivo criado com sucesso!')
