def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')

def aumentar(preço, taxa, format=False):
    preço_final = preço + (preço * taxa / 100)
    return preço_final if not format else moeda(preço_final)


def diminuir(preço, taxa, format=False):
    preço_final = preço - (preço * taxa / 100)
    return preço_final if not format else moeda(preço_final)


def dobro(preço, format=False):
    preço_final = preço * 2
    return preço_final if not format else moeda(preço_final)


def metade(preço, format=False):
    preço_final = preço / 2
    return preço_final if not format else moeda(preço_final)


def resumo(preço=0, taxa_aum=10, taxa_red=5):
    print('-' * 32)
    print('resumo do valor'.upper().center(32))
    print('-' * 32)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, format=True)}')
    print(f'Metade do preço: \t{metade(preço, format=True)}')
    print(f'{taxa_aum}% aumento: \t\t{aumentar(preço, taxa_aum, format=True)}')
    print(f'{taxa_red}% redução: \t\t{diminuir(preço, taxa_red, format=True)}')
    print('-' * 32)
    