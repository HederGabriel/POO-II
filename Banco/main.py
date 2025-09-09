from cliente import Cliente
from conta import Conta

cliente1 = Cliente("Paulo","Silva","123.654.879-10","Rua Sei Lá 200")
cliente2 = Cliente("Fulana","Silva","123.456.789-00","Rua Tal 3789")

c1 = Conta(123,1234,cliente1,1000)
c2 = Conta(321,1234,cliente2,1000)


'''
print("Digite o valor para a opção correspondente: ")
print("0 - Sair")
print("1 - Saque")
print("2 - Transferência")
print("3 - Depósito")
print("4 - Ver extrato")
opcao = int(input())

while 0 <= opcao <= 4:
    if opcao == 0:
        print("Operação finalizada")
        break
    elif opcao == 1:
        valor = float(input("Valor do saque: "))
        status = c1.sacar(valor)
        if status == True:
            print("Saque efetuado com sucesso!")
        else:
            print("Não foi possível efetuar o saque...")
    elif opcao == 2:
        valor = float(input("Valor a ser transferido: "))
        status = c1.transferir(valor, c2)
        if status == True:
            print("Transferência efetuada com sucesso!")
        else:
            print("Não foi possível realizar a transferência...")
    elif opcao == 3:
        valor = float(input("Valor do depósito: "))
        c1.depositar(valor)
    elif opcao == 4:
        print(c1.mostrar_saldo())

    print("Digite o valor para a opção correspondente: ")
    print("0 - Sair")
    print("1 - Saque")
    print("2 - Transferência")
    print("3 - Depósito")
    print("4 - Ver extrato")
    opcao = int(input())
    if (opcao == 0):
        print("Operação finalizada")
        break

'''