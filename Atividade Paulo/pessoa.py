class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")

    def falar(self, mensagem):
        print(f"{self.nome} disse: {mensagem}")
