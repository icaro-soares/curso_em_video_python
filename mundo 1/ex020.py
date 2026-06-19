"""Sorteia uma ordem de alunos"""


from random import shuffle


alunos = []
for c in range(1, 5):
    aluno = input(f'{c}º aluno: ')
    alunos.append(aluno)
shuffle(alunos)
print(f'A ordem de apresentação será: {alunos}')
