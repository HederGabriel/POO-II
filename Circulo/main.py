from circulo import Circulo

def main():
    try:
        raio = float(input("Digite o raio do círculo (maior que 0): "))
        circulo = Circulo(raio)

        print(f"\n=== Resultado do Círculo ===")
        print(f"Raio: {circulo.raio}")
        print(f"Diâmetro: {circulo.calcular_diametro():.2f}")
        print(f"Área: {circulo.calcular_area():.2f}")

    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
