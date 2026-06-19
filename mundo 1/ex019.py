"""Sorteia um aluno de uma lista"""


from random import choice


alunos = []
for c in range(1, 5):
    aluno = input(f'{c}º aluno: ')
    alunos.append(aluno)
print(f'O aluno escolhido foi: {choice(alunos).title()}')
