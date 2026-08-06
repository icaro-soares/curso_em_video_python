def leiaint(msg):
    while True:
        try:
            núm = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um valor válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mO usuário preferiu não digitar o valor.\033[m')
        return núm


def leiafloat(msg):
    while True:
        try:
            núm = float(input(msg).replace(',', '.'))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um valor válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mO usuário preferiu não digitar o valor.\033[m')
        return núm
