'''Faça um Programa que leia 4 notas, mostre as notas e a média na tela'''
notas = []
med = 0
for i in range(1,5):
    nota = float(input(f"Digite a {i} nota: "))
    med += nota
    notas.append([nota])    
med /= 4
print(notas, med)