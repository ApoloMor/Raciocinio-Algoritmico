"""
Adicionando elemento na lista
"""
from os import remove

lista = []
print(lista)
lista.append(10)
print(lista)
lista.append(20)
print(lista)
lista.insert(0, 30)
print(lista)
lista.sort()
print(lista)
lista.extend([4, 6])
print(lista)
del(lista[0])
print(lista)
lista.remove(6)
print(lista)
lista.pop(len(lista)-1)
print(lista)
lista.clear()
print(lista)