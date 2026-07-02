valor = ' '
while True:
    valor = int(input('Valor a sacar: R$ '))
    if valor <= 0:
        print('Erro! Apenas valores válidos.')
    else:
        break
tot = valor
céd = 50
totcéd = 0
while True:
    if tot >= céd:
        tot -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Serão {totcéd} cédulas de R$ {céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if tot == 0:
            break
