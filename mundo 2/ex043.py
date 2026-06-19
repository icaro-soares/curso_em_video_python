alt = float(input('Altura (m): '))
peso = float(input('Peso (kg): '))
imc = peso / alt ** 2
print(f'Seu IMC é: {imc:.1f}')
print('-=' * 30)
if imc < 18.5:
    print('Abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Peso ideal.')
elif 25 <= imc < 30:
    print('Sobrepeso.')
elif 30 <= imc < 40:
    print('Obesidade.')
else:
    print('Obesidade mórbida.')
