cores = (
        '\033[m',
        '\033[0;30;41m',
        '\033[0;30;42m',
        '\033[0;30;43m',
        '\033[0;30;44m',
        '\033[0;30;45m',
        '\033[0;30;46m',
        '\033[0;30;47m',
        '\033[7;30m]',
)

def escreva(msg, cor=0):
    tam = len(msg)
    print(cores[cor], end='')
    print('=' * (tam + 4))
    print(f'{msg.center(tam+4)}')
    print('=' * (tam + 4))
    print(cores[0], end='')

escreva('GUIA DE BIBLIOTECAS PYTHON')

while True:
    opc = input('Função ou biblioteca > ')
    if opc == 'fim':
        escreva('Obrigado!', cor=-3)
        break
    elif opc in dir(__builtins__):
        print(help(opc))
    else:
        escreva('ERRO: O comando não existe!', cor=1)
