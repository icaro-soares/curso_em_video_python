palavras = (
        'ama', 'professor', 'kiwi', 'bolota', 'texto', 'amizade', 'perfeito', 'python', 'guanabara', 'familia',
)
for p in palavras:
    print(f'Vogais em {p.upper()}: ', end='')
    for vogal in p.lower():
        if vogal in 'aeiou':
            print(vogal, end=' ')
    print()
