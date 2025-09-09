from Cliente import Cliente

class Conta:
    def  _init_(self, numero: int, agencia: int, titular: str, saldo:  float ):
        self.numero = numero
        self.agencia  = agencia
        self.titular = titular
        self.saldo =  saldo

    def sacar(self, valor: float):
        if valor > self.saldo:
            return False
        else:
            self.saldo = self.saldo - valor
            return True

    def mostrar_saldo(self):
        return self.saldo

    def depositar(self, valor: float):
        self.saldo = self.saldo + valor
        return True


    def transferir(self, valor: float, contaDestino):
        saque = self.sacar(valor)
        if (saque ==True):
            contaDestino.depositar(valor)
            return True
        else:
            return False


#princial insirando os dados durante a execulção