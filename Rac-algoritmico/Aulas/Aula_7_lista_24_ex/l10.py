''' Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos
valores deverão ser compostos pelos elementos intercalados dos dois outros vetores'''
v1 = []
v2 = []
v3 = []
for i in range (1,11):
    questv1 = int(input(f"Digite o {i} valor para o 1° vetor: "))
    questv2 = int(input(f"Digite o {i} valor para o 2° vetor: "))
    v1.append(questv1)
    v2.append(questv2)
for n in range(10):
    v3.append(v1[n])
    v3.append(v2[n])
print(f"primeiro vetor: {v1},segundo vetor: {v2}, terceiro vetor (intercalado): {v3}")