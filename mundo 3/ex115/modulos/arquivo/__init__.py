def arquivoExiste(nome):
    """
    :param nome: arquivo de texto que a funçao tenta brir
    """
    try:
        # tentativa de abrir o arquivo
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        # se o arquivo não existe retorna False
        return False
    else:
        # Se conseguir achar o arquivo
        return True


def criarArquivo(nome):
    try:
        # tentativa de criar o arquivo, wt+ escreve e adiciona os dados
        a = open(nome, 'wt+')
        a.close()
    except:
        print('\033[0;31mAlgo deu errado na criação do arquivo\033[m')
    else:
        print('\033[0;32mArquivo criado com sucesso!\033[m')
