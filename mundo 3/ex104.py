def leiaInt(msg):
    """
    :param msg: Prompt que recebe a pergunta pro usuário
    :return: retorna um número inteiro válido
    """
    while True:
        n = input(msg)
        if n.isnumeric():
            return int(n)
        else:
            print('Erro! Digite um número!')


n = leiaInt('Digite um número: ')
print(f'Você digitou {n}')
