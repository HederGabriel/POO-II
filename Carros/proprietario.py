from datetime import datetime

# Classe base (herança)
class Pessoa:
    def __init__(self, nome: str, data_nascimento: str):
        self.nome = nome
        self.data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")

    def __str__(self):
        return f"{self.nome} - Nascimento: {self.data_nascimento.strftime('%d/%m/%Y')}"


# Proprietário herda de Pessoa
class Proprietario(Pessoa):
    def __init__(self, nome: str, cpf: str, data_nascimento: str):
        super().__init__(nome, data_nascimento)
        self.cpf = cpf

    def __str__(self):
        return f"Proprietário: {self.nome} | CPF: {self.cpf} | Nascimento: {self.data_nascimento.strftime('%d/%m/%Y')}"
