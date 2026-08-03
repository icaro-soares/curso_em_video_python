def leiaInt(msg):
    while True:
        try:
            n = input(msg).strip()
            if n == '':
                n = 0
                return n
            n = int(n)
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido!\033[m')
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = input(msg).replace(',', '.').strip()
            if n == '':
                n = 0
                return n
            n = float(n)
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número real válido!\033[m')
        else:
            return n
            

núm = leiaInt('Digite um número Inteiro: ')
núm2 = leiaFloat('Digite um número Real: ')
print(f'\033[0;32mVocê digitou o {núm} e {núm2}.\033[m')
