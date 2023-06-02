class ContaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente.")

    def consultar_saldo(self):
        return self.__saldo

conta = ContaBancaria("Davi", 1200)
conta.depositar(700)
conta.sacar(300)
print(conta.consultar_saldo())