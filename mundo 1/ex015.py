"""Calcule o valor de um carro alugado e mostra quanto vai pagar"""
km = float(input('KM: '))
dias = int(input('Dias: '))
preço_total = (dias * 60) + (km * 0.15)
print(f'O valor total pelo carro será de R${preço_total:.2f}'.replace('.', ','))
