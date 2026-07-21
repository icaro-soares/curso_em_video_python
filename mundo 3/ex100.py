from random import randint


def sorteia(lista):
    for c in range(0, 5):
        lista.append(randint(1, 10))


pilha = []
sorteia(pilha)
pilha.sort()
print(f'Números sorteados: {pilha}', )
