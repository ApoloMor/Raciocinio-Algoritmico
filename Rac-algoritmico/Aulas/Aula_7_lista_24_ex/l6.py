'''Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno,
imprima o número de alunos com média maior ou igual a 7.0'''
alunosNaMedia = []
listaMedia = []
media = 0
for aluno in range(10):
    for n in range(1,5):
        nota = float(input(f"Digite a {n} nota: "))
        media += nota
    media /= 4
    if media >= 7:
        alunosNaMedia.append(aluno)
    listaMedia.append(media)
    media = 0
print(f'{len(alunosNaMedia)} ficaram na média! Médias: {[f"{m:.2f}" for m in listaMedia]}')