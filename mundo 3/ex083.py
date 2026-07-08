lista = []
expressão = input('Digite uma expressão matemática com parênteses: ')
for s in expressão:
    if s == '(':
        lista.append(s)
    elif s == ')':
        if len(lista) > 0:
            del lista[-1]
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Expressão válida.')
else:
    print('Expressão inválida.')    
