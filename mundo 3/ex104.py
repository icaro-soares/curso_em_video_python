def leiaInt(msg):
    """
    :param msg: Prompt que recebe a pergunta pro usuário
    :var n: armazena a informação dada pelo usuário, caso seja um número é convertida para um int, se não o programa dá erro, mas continua funcionando
    """
    while True:
        n = input('Digite um número: ')
        if n.isnumeric():
            n = int(n)
        else:
            print('Erro! Digite um número!')


n = leiaInt('Digite um número: ')
print(f'Você digitou {n}')
