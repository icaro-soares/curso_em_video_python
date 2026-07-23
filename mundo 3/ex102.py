def fatorial(n, show=False):
    """
    Mostra o fatorial de um número.
    :Param n: recebe o número que vai mostrar o fatorial
    :Param show: True, valor padrão mostra o processo do calculo; False esconde o processo
    :return m: retorna o valor do fatorial
    """
    m = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        m *= c
    return m


n = int(input('Digite um valor: '))
print(f'Mostrando {n}!: ', end='')
fat = fatorial(n, show=True)
print(fat)
