c = s = 0
while True:
    n = int(input('Digite um valor: [999 p/ parar] '))
    if n == 999:
        break
    else:
        c += 1
        s += n
print('-=' * 30)
print(f'Foram digitados {c} valores, e a soma é {s}')
