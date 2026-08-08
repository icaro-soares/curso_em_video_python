class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo


    def deposito(self, valor):
        self.saldo += valor
        print(f'Depósito de R${valor:.2f}')


    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f'Saque de R${valor:.2f}')
        else:
            print(f'Saque de R${valor:.2f} negado! Saldo insuficiente!')


    def extrato(self):
        print(f'Extrato: R${self.saldo:.2f}')
