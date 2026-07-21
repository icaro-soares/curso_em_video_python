def escreva(txt):
    print('~' * (len(txt) + 4))
    print(f'{txt}'.center(len(txt)+4))
    print('~' * (len(txt) + 4))


escreva('Olá mundo!')
escreva('Eu amo Python!')
escreva('Python!')
escreva('Ícaro Soares')
msg = input('Digite sua mensagem: ')
escreva(msg)
