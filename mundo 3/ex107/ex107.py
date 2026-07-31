import moeda


valor_final = moeda.aumentar(100, 10)
print(f'O valor final a se pagar será R${valor_final:.2f}')
valor_final = moeda.diminuir(100, 10)
print(f'O valor final a se pagar será R${valor_final:.2f}')
valor_final = moeda.dobro(100)
print(f'O valor final a se pagar será R${valor_final:.2f}')
valor_final = moeda.metade(100)
print(f'O valor final a se pagar será R${valor_final:.2f}')
