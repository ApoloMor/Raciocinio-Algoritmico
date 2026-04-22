"""
Adicionando elementos na lista
"""
lista = [0, 5]
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
lista.remove(5)#remove o elemento especifico
print(lista)
lista.pop(1)#remove o elemento por indice e retorna ele mesmo
print(lista)