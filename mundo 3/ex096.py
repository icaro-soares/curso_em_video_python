def area(larg, comp):
    a = larg * comp
    print(f'A área é {a:.2f}cm²')


area(2, 2)
area(15, 25)
area(70, 90)
print('Agora é sua vez')
l = float(input('Largura do terreno (cm): '))
c = float(input('Comprimento do terreno (cm): '))
area(l, c)
