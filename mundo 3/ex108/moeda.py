def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')

def aumentar(preço, taxa):
    preço_final = preço + (preço * taxa / 100)
    return preço_final


def diminuir(preço, taxa):
    preço_final = preço - (preço * taxa / 100)
    return preço_final


def dobro(preço):
    preço_final = preço * 2
    return preço_final


def metade(preço):
    preço_final = preço / 2
    return preço_final
