aluno = []
while True:
    nome = input('Nome: ').strip().title()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    média = (nota1 + nota2)/2
    aluno.append([nome, [nota1, nota2], média])
    resp = ' '
    while resp not in 'SsNn':
        resp = input('Quer continuar? [S/N] ').strip()[0]
    if resp in 'Nn':
        break
print('-=' * 30)
print('boletim'.upper().center(30))
print('-' * 30)
for i, a in enumerate(aluno):
    print(f'{i:<10}{a[0]:^10}{a[2]:>10.1f}')
print('-' * 30)
while True:
    n = int(input('Qual aluno devo mostrar as notas? [999 p/ parar] '))
    if n != 999:
        print(f'Mostrando as notas de {aluno[n][0]} {aluno[n][1]}')
    elif n <= len(aluno) - 1:
        print('Aluno não encontrado!')
    else:
        print('Obrigado!')
        break
