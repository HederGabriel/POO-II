from cliente import Cliente
from conta import Conta

def menu():
    print("\n===== MENU BANCO =====")
    print("1 - Sacar")
    print("2 - Transferir")
    print("3 - Depositar")
    print("4 - Ver Saldo")
    print("0 - Sair")

def main():
    cliente1 = Cliente("Paulo", "Silva", "123.654.879-10", "Rua Sei Lá 200")
    cliente2 = Cliente("Fulana", "Silva", "123.456.789-00", "Rua Tal 3789")

    c1 = Conta(123, 1234, cliente1, 1000)
    c2 = Conta(321, 1234, cliente2, 500)

    while True:
        menu()
        try:
            opcao = int(input("Escolha uma opção: "))
            if opcao == 0:
                print("Operação finalizada. Até logo!")
                break

            elif opcao == 1:
                valor = float(input("Valor do saque: "))
                c1.sacar(valor)

            elif opcao == 2:
                valor = float(input("Valor da transferência: "))
                c1.transferir(valor, c2)

            elif opcao == 3:
                valor = float(input("Valor do depósito: "))
                c1.depositar(valor)

            elif opcao == 4:
                print(c1.mostrar_saldo())

            else:
                print("Opção inválida. Escolha um número entre 0 e 4.")

        except ValueError as erro:
            mensagem = str(erro)
            if "invalid literal" in mensagem:
                print("Por favor, digite apenas números nas opções e valores.")
            elif "Saldo insuficiente" in mensagem:
                print("Você não tem saldo suficiente para essa operação.")
            elif "positivo" in mensagem:
                print("O valor informado precisa ser maior que zero.")
            else:
                print("Algo deu errado com o valor digitado. Tente novamente.")

        except Exception:
            print("Ocorreu um erro inesperado. Tente novamente.")

if __name__ == "__main__":
    main()