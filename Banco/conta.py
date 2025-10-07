from cliente import Cliente

class Conta:
    def __init__(self, numero: int, agencia: int, titular: Cliente, saldo: float):
        self.__numero = numero
        self.__agencia = agencia
        self.__titular = titular
        self.__saldo = saldo

    def sacar(self, valor: float):
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo.")
        if valor > self.__saldo:
            raise ValueError("Saldo insuficiente.")
        self.__saldo -= valor
        return True

    def depositar(self, valor: float):
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser positivo.")
        self.__saldo += valor
        return True

    def transferir(self, valor: float, conta_destino):
        if valor <= 0:
            raise ValueError("O valor da transferência deve ser positivo.")
        if valor > self.__saldo:
            raise ValueError("Saldo insuficiente para transferência.")
        self.__saldo -= valor
        conta_destino.__saldo += valor
        return True

    def mostrar_saldo(self):
        return f"Saldo atual: R$ {self.__saldo:.2f}"

    @property
    def titular(self):
        return self.__titular
