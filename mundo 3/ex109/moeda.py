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
