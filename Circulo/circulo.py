import math
from formas import Forma

class Circulo(Forma):
    def __init__(self, raio: float):
        if raio <= 0:
            raise ValueError("O raio deve ser maior que zero.")
        self.raio = raio

    def calcular_area(self) -> float:
        return math.pi * (self.raio ** 2)

    def calcular_diametro(self) -> float:
        return 2 * self.raio
