class Conta:
    def __init__(self, numero: int, agencia: int, titular: str, saldo_inicial: float):
        self.numero = numero
        self.agencia = agencia
        self.titular = titular
        self.saldo = saldo_inicial

    def sacar(self, valor_saque: float) -> bool:
        if valor_saque <= 0 or valor_saque > self.saldo:
            return False
        self.saldo -= valor_saque
        return True

    def depositar(self, valor_deposito: float) -> bool:
        if valor_deposito <= 0:
            return False
        self.saldo += valor_deposito
        return True

    def mostrar(self) -> bool:
        print(f'{self.titular} - Saldo: R${self.saldo:.2f}')
        return True

    def transferir(self, valor_transferencia: float, destino_nome: str, lista_contas: list) -> bool:
        destino = None
        for conta in lista_contas:
            if conta.titular.lower() == destino_nome.lower() and conta != self:
                destino = conta
                break

        if not destino or valor_transferencia <= 0 or valor_transferencia > self.saldo:
            return False

        self.saldo -= valor_transferencia
        destino.saldo += valor_transferencia
        return True


# ====== FLUXO PRINCIPAL ======

# Criar conta principal
nome_usuario = input("Seu nome completo: ")
numero_conta = int(input("Número da sua conta: "))
agencia_conta = int(input("Número da sua agência: "))
saldo_inicial_usuario = 0

contas_lista = []
c1 = Conta(numero_conta, agencia_conta, nome_usuario, saldo_inicial_usuario)
contas_lista.append(c1)

# Contas fictícias
c2 = Conta(4321, 8765, "Carlos Mendes", 500)
c3 = Conta(9876, 1234, "Ana Lima", 800)
contas_lista.extend([c2, c3])

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
        saque_valor = float(input("Valor para sacar: R$"))
        if c1.sacar(saque_valor):
            print("Saque realizado com sucesso.")
        else:
            print("Erro: saldo insuficiente ou valor inválido.")

    elif opcao == "3":
        transf_valor = float(input("Valor para transferir: R$"))
        nome_destinatario = input("Digite o nome do destinatário: ")
        if c1.transferir(transf_valor, nome_destinatario, contas_lista):
            print("Transferência realizada com sucesso.")
        else:
            print("Erro: destinatário não encontrado, saldo insuficiente ou valor inválido.")

    elif opcao == "4":
        deposito_valor = float(input("Valor para depositar: R$"))
        if c1.depositar(deposito_valor):
            print("Depósito realizado com sucesso.")
        else:
            print("Erro: valor de depósito inválido.")

    elif opcao == "0":
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida. Tente novamente.")
