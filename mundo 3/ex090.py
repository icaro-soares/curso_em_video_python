aluno = {}
aluno['nome'] = input('Nome do aluno(a): ').strip().title()
aluno['média'] = float(input('Média: '))
aluno['situação'] = ' '
if aluno['média'] >= 7:
    aluno['situação'] = 'aprovado(a)'
else:
    aluno['situação'] = 'reprovado(a)'
for k, v in aluno.items():
    print(f'O campo {k} tem valor {v}.')
