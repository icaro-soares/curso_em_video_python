from random import randint
from operator import itemgetter # usado para ordenar o dicionário
from time import sleep

dado = {}
dado['j1'] = randint(1, 6)
dado['j2'] = randint(1, 6)
dado['j3'] = randint(1, 6)
dado['j4'] = randint(1, 6)
for k, v in dado.items():
    sleep(1)
    print(f'{k} tirou {v} no dado.')
print('=' * 30)
print(f'{"ranking".upper():^30}')
print('=' * 30)
ranking = sorted(dado.items(), key=itemgetter(1), reverse=True )
# Retorna uma tupla
for i, v in enumerate(ranking):
    sleep(1)
    print(f'{i+1}º lugar: {v[0]} lugar com {v[1]} ')
