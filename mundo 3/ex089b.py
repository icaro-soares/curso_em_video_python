aluno = {}
dados = {}
while True:
    aluno['nome'] = input('Nome do(a) aluno(a): ').title()
    aluno['n1'] = float(input('Nota 1: '))
    aluno['n2'] = float(input('Nota 2: '))
    aluno['média'] = (aluno['n1']+aluno['n2'])/2
    dados = aluno.copy()
    r = ' '
    while r not in 'sn':
        r = input('Continuar? [s/n] ').lower().strip()
    if r == 'n':
        break
print('-=' * 30)
print(dados)
