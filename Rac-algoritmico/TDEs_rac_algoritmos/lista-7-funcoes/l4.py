'''Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere P,
se seu argumento for positivo, e N, se seu argumento for zero ou negativo.'''
def confere(a):
    if a <= 0:
        return 'N'
    else:
        return 'P'
    
a = int(input('Digite um numero positivo ou negativo: '))
print(confere(a))