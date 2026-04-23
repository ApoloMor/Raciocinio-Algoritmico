#criar uma matriz 3x3 identidade 
#diagonal principal com elementos 

a = []
for  i in range(3):
    a.append([])
    for j in range(3):
        if i == j:
            a[i].append(1)
        else:
            a[i].append(0)
for linha in a:
    print(a)