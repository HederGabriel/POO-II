from proprietario import Proprietario

class Carro:
    def __init__(self, modelo: str, marca: str, ano_fabricacao: int, cor: str, valor: float, proprietario: Proprietario):
        self.modelo = modelo
        self.marca = marca
        self.ano_fabricacao = ano_fabricacao
        self.cor = cor
        self.valor = valor
        self.proprietario = proprietario

    def comprar(self, novo_proprietario: Proprietario):
        """Troca o dono do carro para o novo proprietário"""
        self.proprietario = novo_proprietario

    def __str__(self):
        return (f"\nModelo: {self.modelo}\nMarca: {self.marca}\nAno: {self.ano_fabricacao}\n"
                f"Cor: {self.cor}\nValor: R${self.valor:,.2f}\n{self.proprietario}")
