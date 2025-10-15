from professor import Professor
from aluno import Aluno

def main():
    # Criando um professor e dois alunos
    professor = Professor("Carlos Silva", 40, "Matemática")
    aluno1 = Aluno("Ana", 17)
    aluno2 = Aluno("João", 16)

    # O professor fala algo
    professor.falar("Vamos começar a aula de hoje sobre equações do segundo grau!")

    # O professor atribui notas
    professor.atribuir_nota(aluno1, 9.0)
    professor.atribuir_nota(aluno2, 7.5)

    print("\n=== Informações dos Alunos ===")
    aluno1.exibir_informacoes()
    print("-------------------------------")
    aluno2.exibir_informacoes()

    print("\n=== Informações do Professor ===")
    professor.exibir_informacoes()

if __name__ == "__main__":
    main()
