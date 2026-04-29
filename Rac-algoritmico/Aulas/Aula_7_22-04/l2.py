'''Criar um programa que solicite ao usuário 2 listas com 5
elementos cada. Como resultado, criar uma terceira lista que
intercala os elementos das duas listas.'''
l3 = []
cont = 1
while cont < 7:
    i1 = input(f"digite o {cont} elemento:")
    l1 = [i1]
    i2 = input(f"digite o {cont} elemento:")
    l2 = [i2]
    for i in l1:
        l3.append(i)
        for j in l2:
            l3.append(j)
    cont += 1
print(l3)