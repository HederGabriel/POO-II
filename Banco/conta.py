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

    def depositar(self, valor: float):
        self.saldo += valor
        print("Deposito realizado")

    def mostrar(self):
        print(f'{self.titular} - Saldo: R${self.saldo:.2f}')

    def transferir(self, valor: float, destino):
        if valor > self.saldo:
            print("Saldo insuficiente para transferir")
        else:
            self.saldo -= valor
            destino.saldo += valor
            print(f'Transferência de R${valor:.2f} para {destino.titular} realizada com sucesso.')


# Criar contas
nome = input("Seu nome completo: ")
num = int(input("Número da sua conta: "))
ag = int(input("Número da sua agência: "))
saldo = 0

# Lista de contas
contas = []

# Conta principal do usuário
c1 = Conta(num, ag, nome, saldo)
contas.append(c1)

# Outras contas fictícias
c2 = Conta(4321, 8765, "Carlos Mendes", 500)
c3 = Conta(9876, 1234, "Ana Lima", 800)
contas.extend([c2, c3])

# Menu de opções
while True:
    print("\n----- MENU -----")
    print("1. Mostrar meu saldo")
    print("2. Sacar")
    print("3. Transferir")
    print("4. Depositar")
    print("5. Mostrar todos os saldos")
    print("0. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        c1.mostrar()
    elif opcao == "2":
        valor = float(input("Valor para sacar: R$"))
        c1.sacar(valor)
    elif opcao == "3":
        valor = float(input("Valor para transferir: R$"))
        destNome = input("Digite o nome do destinatário: ")

        # Buscar destinatário pela lista de contas
        destino = None
        for conta in contas:
            if conta.titular.lower() == destNome.lower() and conta != c1:
                destino = conta
                break

        if destino:
            c1.transferir(valor, destino)
        else:
            print("Destinatário não encontrado.")
    elif opcao == "4":
        valorDeposito = float(input("Valor para depositar: R$"))
        c1.depositar(valorDeposito)
    elif opcao == "5":
        print("\n--- SALDOS DAS CONTAS ---")
        for conta in contas:
            conta.mostrar()
    elif opcao == "0":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")
