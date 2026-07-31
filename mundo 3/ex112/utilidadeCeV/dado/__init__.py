def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = input(msg).replace(',', '.').strip()
        if entrada.replace('.', '', 1).isdigit(): 
            valido = True
            return float(entrada)
        else:
            print('ERRO! Digite um valor válido!')
            