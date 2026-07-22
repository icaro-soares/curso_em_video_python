from random import randint


def sorteia(lista):
    for c in range(0, 5):
        lista.append(randint(1, 10))


def somaPar(lista):
    s = 0
    for num in lista:
        if num % 2 == 0:
            print(num, end=' ')
            s += num
    print(f'\nA soma é {s}')


pilha = []
sorteia(pilha)
pilha.sort()
print(f'Números sorteados: {pilha}', )
print('Os números pares foram: ', end='')
somaPar(pilha)
