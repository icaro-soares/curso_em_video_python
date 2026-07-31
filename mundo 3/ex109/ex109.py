import moeda


valor = float(input('Digite o valor: '))
valor_final = moeda.aumentar(valor, 10, format=True)
print(valor_final)
