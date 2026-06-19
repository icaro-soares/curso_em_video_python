"""Lê três retas e diz se podem formar um triângulo, em caso de sim, diz qual
o tipo de triângulo formado"""
r1 = int(input('Reta 1: '))
r2 = int(input('Reta 2: '))
r3 = int(input('Reta 3: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Pode formar um triângulo!')
    if r1 == r2 == r3:
        print('Triângulo equilátero!')
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print('Triângulo isóceles!')
    else:
        print('Triângulo escaleno!')
else:
    print('Não pode formar um triângulo!')
