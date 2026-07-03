times = (
        'palmeiras', 'flamengo', 'fluminense', 'athletico-PR', 'bragantino', 'bahia', 'coritiba', 'são paulo', 'atlético-MG', 'corinthians', 'cruzeiro', 'botafogo', 'vitória', 'internacional', 'santos', 'santos', 'grêmio', 'vasco', 'remo', 'mirassol', 'chapecoense',
)
print('Os 5 primeiros times são:')
for time in times[:5]:
    print(f'\t{time.title()}')
print('-=' * 30)
print('Os últimos 4 colocados são:')
for time in times[-4:]:
    print(f'\t{time.title()}')
print('-=' * 30)
print('Times em ordem alfabética:')
for time in sorted(times):
    print(f'\t{time}')
print('-=' * 30)
print(f'O time chapecoense está na {times.index('chapecoense')}ª posição.')
