from pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self.disciplina = disciplina

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Disciplina: {self.disciplina}")

    def atribuir_nota(self, aluno, nota):
        aluno.notas.append(nota)
        print(f"O professor {self.nome} atribuiu a nota {nota} ao aluno {aluno.nome}.")
