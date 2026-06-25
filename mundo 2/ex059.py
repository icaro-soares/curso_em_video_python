from time import sleep


n1 = int(input('1º valor: '))
n2 = int(input('2º valor: '))
while True:
    opc = int(input("""O que devo fazer: 
        [1 - Somar]
        [2 - Multiplicar]
        [3  Maior]
        [4 - Novos números]
        [5 - Sair do programa] """))
    if opc == 5:
        print('Saindo...')
        sleep(1)
        break
    elif opc == 1:
        soma = n1 + n2
        print(f'A soma é {soma}.')
    elif opc == 2:
        multi = n1 * n2
        print(f'O produto é {multi}.')
    elif opc == 3:
        if n1 > n2:
            print('O primeiro valor é maior.')
        elif n1 < n2:
            print('O segundo valor é maior.')
        else:
            print('O valores são iguais.')
    elif opc == 4:
        print('Insira novos valores.')
        n1 = int(input('1º valor: '))
        n2 = int(input('2º valor: '))
