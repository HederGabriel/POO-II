from proprietario import Proprietario
from carro import Carro

def main():
    # Criando proprietários
    proprietario1 = Proprietario("João Silva", "111.111.111-11", "10/01/1985")
    proprietario2 = Proprietario("Maria Oliveira", "222.222.222-22", "20/03/1990")

    # Criando carros
    carro1 = Carro("Civic", "Honda", 2020, "Preto", 120000.00, proprietario1)
    carro2 = Carro("Corolla", "Toyota", 2018, "Branco", 95000.00, proprietario2)

    print("=== Situação Inicial ===")
    print("Carro 1:", carro1)
    print("Carro 2:", carro2)

    # Proprietário 1 compra o carro do Proprietário 2
    carro2.comprar(proprietario1)

    print("\n=== Após a Compra ===")
    print("Carro 1:", carro1)
    print("Carro 2:", carro2)


if __name__ == "__main__":
    main()
