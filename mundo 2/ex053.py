frase = input('Digite algo [sem acentos]: ').strip().upper().split()
frase = ''.join(frase)
if frase == frase[::-1]:
    print('A frase (palavra) é um palíndromo!')
else:
    print('A frase (palavra) não é um palíndromo!')
