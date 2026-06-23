from datetime import date


maior = menor = 0
for c in range(1, 8):
    ano = int(input(f'Ano de nascimento da {c}ª pessoa: '))
    if date.today().year - ano < 21:
        menor += 1
    else:
        maior += 1
print(f'Pessoas maiores de idade: {maior}\nPessoas menores de idade: {menor}')
