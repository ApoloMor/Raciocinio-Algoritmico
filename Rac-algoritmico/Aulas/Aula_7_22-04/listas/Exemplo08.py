"""
Criar uma matriz 3x3 identidade
Diagonal principal com elementos iguais a 1 (i == j)
Demais elementos, 0
"""
a = []
for i in range(3):
    a.append([])
    for j in range(3):
        if i == j:
            a[i].append(1)
        else:
            a[i].append(0)
for linha in a:
    print(linha)