"""Cálcula a área de uma parede e diz quantos litros de tinta precisa para pintá-la"""
alt = float(input('Altura da parede (m): '))
larg = float(input('Largura da parede (m): '))
area = alt*larg
tinta = area/2
print(f'Para pintar uma parede de {area:.2f}m² serão necessários {tinta:.1f}L de tinta.')