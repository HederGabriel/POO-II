from cliente import Cliente

class Conta:

    def __init__(self, numero: int, agencia: int, titular: Cliente, saldo: float):
        self.__numero = numero
        self.__agencia = agencia
        self.__titular = titular
        self.__saldo = saldo

    def __sacar(self, valor: float):
        if valor > self.__saldo:
            return False
        else:
            self.__saldo = self.__saldo - valor
            return True

    def __mostrar_saldo(self):
        return self.__saldo

    def __depositar(self, valor: float):
        self.__saldo = self.__saldo + valor
        return None

    def __transferir(self, valor: float, contaDestino):
        saque = self.__sacar(valor)
        if saque:
            contaDestino.__depositar(valor)
            return True
        else:
            return False











'''
c1 = Conta(123,4321,"Paulo",1000)
c2 = Conta(321,2468,"Ana",1000)

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
        senha = input("Digite a senha para confirmar a operação: ")
        status = c1.__sacar(valor,senha)
        if status == True:
            print("Saque efetuado com sucesso!")
        else:
            print("Não foi possível efetuar o saque...")
    elif opcao == 2:
        valor = float(input("Valor a ser transferido: "))
        destino = input("Digite o usuário da conta de destino: ")
        senha = input("Digite a senha para confirmar a operação: ")
        if clienteAndre.get_user() == destino:
            status = contaPaulo.__transferir(contaAndre, valor, senha)
            if status == True:
                print("Transferência efetuada com sucesso!")
            else:
                print("Não foi possível realizar a transferência...")
        else:
            print("Nome do usuário de destino está incorreto ou é inexistente!")
    elif opcao == 3:
        valor = float(input("Valor do depósito: "))
        senha = input("Digite a senha para confirmar a operação: ")
        contaPaulo.__depositar(valor, senha)
    elif opcao == 4:
        senha = input("Digite a senha para confirmar a operação: ")
        print(contaPaulo.extrato(senha))

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
