class Conta:
    def __init__(self, numero: int, agencia: int, titular: str, saldo: float):
        self.numero = numero
        self.agencia = agencia
        self.titular = titular
        self.saldo = saldo

    def sacar(self, valor: float) -> bool:
        if valor <= 0 or valor > self.saldo:
            return False
        self.saldo -= valor
        return True

    def depositar(self, valor: float) -> bool:
        if valor <= 0:
            return False
        self.saldo += valor
        return True

    def mostrar(self) -> bool:
        # Apenas exibe — sempre retorna True
        print(f'{self.titular} - Saldo: R${self.saldo:.2f}')
        return True

    def transferir(self, valor: float, destNome: str, contas: list) -> bool:
        # Localiza destino
        destino = None
        for conta in contas:
            if conta.titular.lower() == destNome.lower() and conta != self:
                destino = conta
                break

        if not destino or valor <= 0 or valor > self.saldo:
            return False

        self.saldo -= valor
        destino.saldo += valor
        return True


# ====== FLUXO PRINCIPAL ======

# Criar conta principal
nome = input("Seu nome completo: ")
num = int(input("Número da sua conta: "))
ag = int(input("Número da sua agência: "))
saldo = 0

contas = []
c1 = Conta(num, ag, nome, saldo)
contas.append(c1)

# Contas fictícias
c2 = Conta(4321, 8765, "Carlos Mendes", 500)
c3 = Conta(9876, 1234, "Ana Lima", 800)
contas.extend([c2, c3])

while True:
    print("\n----- MENU -----")
    print("1. Mostrar meu saldo")
    print("2. Sacar")
    print("3. Transferir")
    print("4. Depositar")
    print("0. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        c1.mostrar()

    elif opcao == "2":
        valor = float(input("Valor para sacar: R$"))
        if c1.sacar(valor):
            print("Saque realizado com sucesso.")
        else:
            print("Erro: saldo insuficiente ou valor inválido.")

    elif opcao == "3":
        valor = float(input("Valor para transferir: R$"))
        destNome = input("Digite o nome do destinatário: ")
        if c1.transferir(valor, destNome, contas):
            print("Transferência realizada com sucesso.")
        else:
            print("Erro: destinatário não encontrado, saldo insuficiente ou valor inválido.")

    elif opcao == "4":
        valorDeposito = float(input("Valor para depositar: R$"))
        if c1.depositar(valorDeposito):
            print("Depósito realizado com sucesso.")
        else:
            print("Erro: valor de depósito inválido.")

    elif opcao == "0":
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida. Tente novamente.")
