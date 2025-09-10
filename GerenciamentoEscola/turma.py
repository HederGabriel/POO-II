class Turma:
    def __init__(self, codigo: str, serie: str, turno: str):
        self._codigo = codigo
        self._serie = serie
        self._turno = turno
        self._alunos = []
        self._professor = None

    # Getters e Setters
    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        self._codigo = valor

    @property
    def serie(self):
        return self._serie

    @serie.setter
    def serie(self, valor):
        self._serie = valor

    @property
    def turno(self):
        return self._turno

    @turno.setter
    def turno(self, valor):
        self._turno = valor

    @property
    def alunos(self):
        return self._alunos

    @property
    def professor(self):
        return self._professor

    @professor.setter
    def professor(self, valor):
        self._professor = valor

    # Métodos
    def adicionar_aluno(self, aluno):
        self._alunos.append(aluno)
        aluno.turma = self

    def definir_professor(self, professor):
        self._professor = professor
        professor.turma = self

    def mudar_turno(self, novo_turno: str):
        self._turno = novo_turno

    def __str__(self):
        alunos_str = ", ".join([aluno.nome for aluno in self._alunos]) if self._alunos else "Nenhum aluno"
        prof_str = self._professor.nome if self._professor else "Sem professor"
        return f"Turma: {self._codigo} - Série: {self._serie} - Turno: {self._turno}\nProfessor: {prof_str}\nAlunos: {alunos_str}\n"
