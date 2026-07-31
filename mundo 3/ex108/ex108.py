import moeda


p = float(input('Digite o preço: '))
print(f'O valor digitado foi {moeda.moeda(p)}')
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
