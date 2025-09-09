from Cliente import Cliente
from conta import Conta

nome = input("nome completo:")
sobrenome = input("sobrenome:")
cpf = input("cpf:")
endereco = input("endereço:")

cliente1 = Cliente(nome,sobrenome,cpf,endereco)
cliente2 = Cliente("fulana","Silva","123.456.789-00","Rua tal 2345")

num = int(input("número da conta:"))
ag =  int(input("número da agencia:"))
saldo = 500

c1 =  Conta(num,ag,nome,saldo)
c2 = Conta(3523,2141,"bill",3000)

while True:
    print("\n--- Menu ---")
    print("1 - Mostrar Saldo")
    print("2 - Sacar")
    print("3 - Depositar")
    print("4 - Transferir")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        c1.mostrar_saldo()

    elif opcao == "2":
        valor = float(input("Valor para saque: R$"))
        if c1.sacar(valor):
            print("Saque realizado com sucesso.")
        else:
            print("Saldo insuficiente.")

    elif opcao == "3":
        valor = float(input("Valor para depósito: R$"))
        c1.depositar(valor)

    elif opcao == "4":
        valor = float(input("Valor para transferência: R$"))
        c1.transferir(valor, c2)

    elif opcao == "0":
        print("Encerrando o sistema. Até logo!")
        break

    else:
        print("Opção inválida. T4ente novamente.")