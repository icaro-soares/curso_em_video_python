boletim = []
alunos = {}
while True:
    alunos['nome'] = input('Nome: ').strip()
    alunos['nota1'] = float(input('Nota 1: '))
    alunos['nota2'] = float(input('Nota 2: '))
    alunos['média'] = (alunos['nota1'] + alunos['nota2'])/2
    boletim.append(alunos.copy())
    r = ' '
    while r not in 'SsNn':
        r = input('Quer continuar? [S/N] ').strip()[0]
    if r in 'Nn':
        break
print('-=' * 30)
for i, v in enumerate(boletim):
    print(f'')
