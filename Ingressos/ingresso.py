class Ingresso:
    def __init__(self, valor):
        self.valor = valor

    def imprimeValor(self):
        print(f"Valor do ingresso: R${self.valor:.2f}")
