'''Criar um programa que receba uma lista de números e retorne a
média dos mesmos.'''
def media(*numeros):
    return sum(numeros) / len(numeros)
listaNumeros = media(4, 6, 8,)
print(listaNumeros)