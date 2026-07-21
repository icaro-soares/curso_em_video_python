from time import sleep

def contador(i, f, p=1):
    cont = i
    if p == 0:
        p = 1
    if i < f:
        while cont <= f:
            print(cont, end=' ', flush=True)
            sleep(.5)
            cont += abs(p)
        print()
    else:
        while cont >= f:
            print(cont, end=' ', flush=True)
            sleep(.5)
            cont -= abs(p)
        print()


print('Contagem de 1 até 10 de 1 em 1')
contador(1, 10)
print('-=' * 30)
print('Contagem de 10 até 0 voltando de 2 em 2')
contador(10, 0, 2)
print('-=' * 30)
print('Tente você agora!')
ini = int(input('Valor inicial da contagem: '))
fim = int(input('Valor final da contagem: '))
passo = int(input('Passo da contagem: '))
contador(ini, fim, passo)
print('-=' * 30)
