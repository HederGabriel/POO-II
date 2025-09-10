from turma import Turma

class Professor:
    def __init__(self, nome: str, matricula: str):
        self._nome = nome
        self._matricula = matricula
        self._turma = None

    # Getters e Setters
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor

    @property
    def matricula(self):
        return self._matricula

    @matricula.setter
    def matricula(self, valor):
        self._matricula = valor

    @property
    def turma(self):
        return self._turma

    @turma.setter
    def turma(self, nova_turma: Turma):
        self._turma = nova_turma

    # Métodos
    def mudar_turma(self, nova_turma: Turma):
        if self._turma:
            self._turma.professor = None
        nova_turma.definir_professor(self)

    def __str__(self):
        turma_str = self._turma.codigo if self._turma else "Sem turma"
        return f"Professor: {self._nome}, Matrícula: {self._matricula}, Turma: {turma_str}"
 