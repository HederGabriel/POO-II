from vip import VIP

class CamaroteInferior(VIP):
    def __init__(self, valor, adicional, localizacao):
        super().__init__(valor, adicional)
        self.localizacao = localizacao

    def imprimeLocalizacao(self):
        print(f"Localização do camarote inferior: {self.localizacao}")
