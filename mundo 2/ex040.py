"""Calcula a média de um aluno e imprime a situação"""
n1 = float(input('1ª nota: '))
n2 = float(input('2ª nota: '))
m = (n1 + n2) / 2
print(f'Média do aluno: {m:.1f}')
print('-=' * 30)
if m < 5.0:
    print('Reprovado!')
elif 5.0 <= m < 7:
    print('Recuperação!')
else:
    print('Aprovado!')
