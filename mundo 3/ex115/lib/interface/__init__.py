from ex113 import leia


def linha(tam=42):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42).upper())
    print(linha())

def menu(lista):
    cabecalho('menu principal')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leia.leiaInt()
    return opc