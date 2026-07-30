cores = (
        '\033[m', # fundo branco
        '\033[0; 30; 41m', # fundo vermelho
        '\033[0; 30; 42m', # fundo verde
        '\033[0; 30; 43m', # fundo amarelo
        '\033[0; 30; 44m', # fundo azul
        '\033[0; 30; 45m', # fundo violeta
        '\033[0; 30; 46m', # fundo azul anil
        '\033[0; 30; 47m', # fundo cinza
        '\033[7; 30m' # inversão de cores
)

def titulo(msg, cor=0):
    tam = len(msg)

    print('=' * (tam + 4))
    print(f'{msg.center(tam+4)}')
    print('=' * (tam + 4))


