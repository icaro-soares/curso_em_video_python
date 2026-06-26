while True:
    n = int(input('Digite um número: [número < 0 p/ parar] '))
    if n < 0:
        break
    else:
        print(f'Mostrando a tabuada de {n}'.center(30))
        print('=' * 30)
        for c in range(1, 11):
            print(f'{c:2} x {n:3} = {c*n:3}'.center(30))
