"""Calcula a hipotenusa de um triângulo"""


from math import hypot


co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
print(f'A hipotenusa é {hypot(co, ca):.2f}cm')
