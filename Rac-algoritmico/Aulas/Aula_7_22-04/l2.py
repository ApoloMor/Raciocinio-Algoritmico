'''Criar um programa que solicite ao usuário 2 listas com 5
elementos cada. Como resultado, criar uma terceira lista que
intercala os elementos das duas listas.'''
l3 = [ ]
cont = 0
while cont < 6:
    i1 = input("digite um elemento:")
    l1 = [i1]
    i2 = input("digite um elemento:")
    l2 = [i2]
    cont += 1

for i in l1:
    l3.append(i)
    for j in l2:
        l3.append(j)
print(l1, l2, l3)