from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.notas = []

    def exibir_informacoes(self):
        super().exibir_informacoes()
        self.mostrar_notas()

    def mostrar_notas(self):
        if self.notas:
            print(f"Notas: {', '.join(map(str, self.notas))}")
        else:
            print("Nenhuma nota cadastrada.")
