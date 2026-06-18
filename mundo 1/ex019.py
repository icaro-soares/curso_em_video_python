from random import choice


aluno1 = input('1º aluno: ')
aluno2 = input('2º aluno: ')
aluno3 = input('3º aluno: ')
aluno4 = input('4º aluno: ')
alunos = [aluno1, aluno2, aluno3, aluno4]
print(f'O aluno escolhido foi: {choice(alunos).title()}')
