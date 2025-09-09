from abc import ABC, abstractmethod
import math

class Forma(ABC):
    """Classe abstrata para representar formas geométricas"""

    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def calcular_diametro(self):
        pass
