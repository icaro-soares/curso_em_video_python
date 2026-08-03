def leiaInt(msg):
    while True:
        try:
            núm = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um valor válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mO usuário preferiu não digitar o valor.\033[m')
        return núm


def leiaFloat(msg):
    while True:
        try:
            núm = float(input(msg).replace(',', '.'))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um valor válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mO usuário preferiu não digitar o valor.\033[m')
        return núm

n1 = leiaInt('Digite um valor: ')
n2 = leiaFloat('Digite outro valor: ')
print(f'\033[0;32mO valor inteiro digitado foi {n1}, e o valor Real foi {n2}\033[m')
 