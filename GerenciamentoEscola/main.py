# main.py
from aluno import Aluno
from professor import Professor
from turma import Turma
import time

def etapa(n, msg):
    print(f"\n=== Etapa {n}: {msg} ===")

if __name__ == "__main__":
    step = 1

    etapa(step, "Criação das turmas")
    step += 1
    turma1 = Turma("3° TI", "3° Ano", "Matutino")
    print(f"  -> Criada: {turma1.codigo} ({turma1.serie}) - Turno: {turma1.turno}")
    turma2 = Turma("2° TI", "2° Ano", "Vespertino")
    print(f"  -> Criada: {turma2.codigo} ({turma2.serie}) - Turno: {turma2.turno}")

    etapa(step, "Criação dos alunos")
    step += 1
    aluno1 = Aluno("Heder", "11111111111", "A001"); print(f"  -> Aluno criado: {aluno1.nome} ({aluno1.matricula})")
    aluno2 = Aluno("Taylana", "22222222222", "A002"); print(f"  -> Aluno criado: {aluno2.nome} ({aluno2.matricula})")
    aluno3 = Aluno("Gustavo", "33333333333", "A003"); print(f"  -> Aluno criado: {aluno3.nome} ({aluno3.matricula})")
    aluno4 = Aluno("Rickaelly", "44444444444", "A004"); print(f"  -> Aluno criado: {aluno4.nome} ({aluno4.matricula})")
    aluno5 = Aluno("Miguel", "55555555555", "A005"); print(f"  -> Aluno criado: {aluno5.nome} ({aluno5.matricula})")

    etapa(step, "Criação dos professores")
    step += 1
    prof1 = Professor("Paulo", "P001"); print(f"  -> Professor criado: {prof1.nome} ({prof1.matricula})")
    prof2 = Professor("Tiba", "P002");  print(f"  -> Professor criado: {prof2.nome} ({prof2.matricula})")

    etapa(step, "Associando alunos às turmas (3 alunos na 3°, 2 alunos na 2°)")
    step += 1
    print(f"  -> Adicionando {aluno1.nome} à {turma1.codigo}"); turma1.adicionar_aluno(aluno1)
    print(f"  -> Adicionando {aluno2.nome} à {turma1.codigo}"); turma1.adicionar_aluno(aluno2)
    print(f"  -> Adicionando {aluno3.nome} à {turma1.codigo}"); turma1.adicionar_aluno(aluno3)

    print(f"  -> Adicionando {aluno4.nome} à {turma2.codigo}"); turma2.adicionar_aluno(aluno4)
    print(f"  -> Adicionando {aluno5.nome} à {turma2.codigo}"); turma2.adicionar_aluno(aluno5)

    etapa(step, "Associando cada professor a uma turma")
    step += 1
    print(f"  -> Associando {prof1.nome} à {turma1.codigo}"); turma1.definir_professor(prof1)
    print(f"  -> Associando {prof2.nome} à {turma2.codigo}"); turma2.definir_professor(prof2)

    etapa(step, "Professores vão trocar de turma")
    step += 1
    print(f"  -> Movendo {prof1.nome} para {turma2.codigo}"); prof1.mudar_turma(turma2)
    print(f"  -> Movendo {prof2.nome} para {turma1.codigo}"); prof2.mudar_turma(turma1)

    etapa(step, "Mudando o turno da turma 2° TI para Noturno")
    step += 1
    print(f"  -> Turno atual de {turma2.codigo}: {turma2.turno}")
    turma2.mudar_turno("Noturno")
    print(f"  -> Novo turno de {turma2.codigo}: {turma2.turno}")

    etapa(step, "Resumo final — Turmas, Alunos e Professores (visão completa)")
    step += 1
    print("\n--- INFORMAÇÕES DAS TURMAS ---")
    print(turma1)
    print(turma2)

    print("--- INFORMAÇÕES DOS ALUNOS ---")
    for aluno in [aluno1, aluno2, aluno3, aluno4, aluno5]:
        print(" ", aluno)

    print("\n--- INFORMAÇÕES DOS PROFESSORES ---")
    for prof in [prof1, prof2]:
        print(" ", prof)
