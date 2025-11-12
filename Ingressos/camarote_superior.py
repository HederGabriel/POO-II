from vip import VIP

class CamaroteSuperior(VIP):
    def __init__(self, valor, adicional, adicionalSuperior):
        super().__init__(valor, adicional)
        self.adicionalSuperior = adicionalSuperior

    def valorCamaroteSuperior(self):
        return self.valor + self.adicional + self.adicionalSuperior
