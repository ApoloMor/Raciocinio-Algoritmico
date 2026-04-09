"""Criar um programa que gera a série de Fibonacci até enquanto o
valor for menor que um valor informado pelo usuário. Obs.: Série de
Fibonacci = 0, 1, 1, 2, 3, 5, 8 ,13, 21, 34, 55,... é formada por 0, 1 e
partir deste ponto sempre será a soma dos dois valores anteriores.
"""
limite = int(input("Digite o limite da geração da série de Fibonacci:"))
anterior = 1
for i in range (1,limite):
    i += anterior
    print (i)