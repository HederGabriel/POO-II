class Conta:
    def __init__(self, numero: int, agencia: int, titular: str, saldo: float):
        self.numero = numero
        self.agencia = agencia
        self.titular = titular
        self.saldo = saldo

    def sacar(self, valor: float):
        if valor > self.saldo:
            print("Saldo insuficiente")
        else:
            self.saldo -= valor
            print("Saque realizado")

    def mostrar(self):
        print(f'{self.titular} - Saldo: R${self.saldo:.2f}')

    def transferir(self, valor: float, destino):
        if valor > self.saldo:
            print("Saldo insuficiente para transferir")
        else:
            self.saldo -= valor
            destino.saldo += valor
            print(f'Transferência de R${valor:.2f} para {destino.titular} realizada com sucesso.')

nome = input("Seu nome completo: ")
num = int(input("Número da sua conta: "))
ag = int(input("Número da sua agência: "))
saldo = 0

c1 = Conta(num, ag, nome, saldo)
c1.saldo = 1000

c2 = Conta(4321, 8765, "Carlos Mendes", 0)

print("")
qnt = float(input("Valor do saque: "))
c1.sacar(qnt)
c1.mostrar()

print("")
valor_transferencia = float(input("Digite o valor da transferência: "))
dest_nome = input("Digite quem vai receber sua transferência: ")

if dest_nome == c2.titular:
    c1.transferir(valor_transferencia, c2)
else:
    print("Destinatário não encontrado.")

print("\nSaldos Atualizados")
c1.mostrar()
c2.mostrar()
