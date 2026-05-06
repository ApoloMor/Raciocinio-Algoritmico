'''Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de
13 anos possuem altura inferior à média de altura desses alunos.'''
idadeAlunos = [10, 11, 12, 13, 14, 15, 16, 12, 13, 11,
          14, 15, 10, 16, 12, 13, 11, 14, 15, 10,
          16, 12, 13, 11, 14, 15, 10, 16, 12, 13]

alturaAlunos = [1.40, 1.45, 1.50, 1.55, 1.60, 1.65, 1.70, 1.52, 1.57, 1.46,
           1.62, 1.67, 1.41, 1.72, 1.51, 1.56, 1.47, 1.63, 1.68, 1.42,
           1.73, 1.53, 1.58, 1.48, 1.64, 1.69, 1.43, 1.74, 1.54, 1.59]
media = sum(alturaAlunos) / len(alturaAlunos)
contador = 0
for i in range(len(idadeAlunos)):
    if idadeAlunos[i] > 13 and alturaAlunos[i] < media:
        contador += 1
print(f"{contador} alunos com mais de 13 anos estão abaixo da média de altura.")