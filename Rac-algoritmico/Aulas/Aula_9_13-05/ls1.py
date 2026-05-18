'''Criar um programa que calcula a partir de uma função o fatorial
de um número. Exemplo: Fatorial de 5 => 5! = 5.4.3.2.1. Obs.:
Por propriedade, 0! = 1.'''

def fatorial(num):
    resultado = 1
    for n in range(1, num + 1):
        resultado *= n
    return resultado
num = int(input('digite um numero: '))
fat = fatorial(num)
print(fat)