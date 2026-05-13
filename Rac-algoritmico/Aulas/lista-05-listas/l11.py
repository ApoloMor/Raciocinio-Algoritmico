''' Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos
valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
Altere o programa anterior, intercalando 3 vetores de 10 elementos cada'''
v1 = []
v2 = []
v3 = []
v4 = []
for i in range (1,11):
    questv1 = int(input(f"Digite o {i} valor para o 1° vetor: "))
    questv2 = int(input(f"Digite o {i} valor para o 2° vetor: "))
    questv3 = int(input(f"Digite o {i} valor para o 3° vetor: "))
    v1.append(questv1)
    v2.append(questv2)
    v3.append(questv3)
for n in range(10):
    v4.append(v1[n])
    v4.append(v2[n])
    v4.append(v3[n])
print(f"Primeiro vetor: {v1}\nSegundo vetor: {v2}\nTerceiro vetor: {v3}\nQuarto vetor: {v4}")