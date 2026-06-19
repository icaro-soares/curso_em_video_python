"""Calcula o seno, cosseno e tangente de um ângulo"""


from math import sin, cos, tan, radians


ang = float(input('Digite um ângulo qualquer: '))
seno = sin(radians(ang))
cosseno = cos(radians(ang))
tangente = tan(radians(ang))
print(f'Seno de {ang}º: {seno:.2f}º\nCosseno de {ang}º: {cosseno:.2f}\nTangente'
      f' de {ang}º: {tangente:.2f}')
