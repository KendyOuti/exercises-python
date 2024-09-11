'''Faça um programa que leia nomes de alunos e suas respectivas notas até que o 
nome ’oooo’ seja informado, após o fim da leitura, exiba o nome do aluno que possui 
a maior nota. Obs.: Use dicionário para resolver essa questão. '''

def maior_nota():
    nome = " "
    aluno_maior_nota = " "
    alunos_notas = {}
    while nome != "oooo":
        nome = str(input("Nome: "))
        if nome == "oooo":
            break
        else:
            alunos_notas[nome] = int(input("Nota: "))

    for c, v in alunos_notas.items():
        if v == max(alunos_notas.values()):
            aluno_maior_nota = c
            break

    return aluno_maior_nota, max(alunos_notas.values())

def main():
    aluno, nota = maior_nota()
    print(f"O aluno {aluno} tirou a maior nota, igual a {nota}")

main()