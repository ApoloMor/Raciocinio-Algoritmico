'''Criar um programa que calcula o fatorial de um número, mas de
forma recursiva, ou seja, chamando a própria função fatorial de
dentro dela mesma.'''
def fatorial_rec(numero):
    if numero == 0:
        return 1
    return numero * fatorial_rec(numero -1)

numero = int(input("Digite um numero: "))
fatorial = fatorial_rec(numero)
print(f'O fatorial de {numero} é: {fatorial}')