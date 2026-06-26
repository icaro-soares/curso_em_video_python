s = c = 0
while True:
    n = int(input('Digite um valor: [999 p/ parar] '))
    if n != 999:
        c += 1
        s += n
    else:
        print(f'Foram digitados {c} valores, e a soma deles é {s}.')
        break
