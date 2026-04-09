"""Criar um programa que gera a série de Fibonacci até enquanto o
valor for menor que um valor informado pelo usuário. Obs.: Série de
Fibonacci = 0, 1, 1, 2, 3, 5, 8 ,13, 21, 34, 55,... é formada por 0, 1 e
partir deste ponto sempre será a soma dos dois valores anteriores.
"""
while True:
    try:
        limite = int(input("Digite o limite da geração da série de Fibonacci: "))
    except:
        print("Digite um número válido.")
        continue
    serie = 0
    anterior = 1
    while serie < limite:
        print(serie, end=" , ")
        proximo = serie + anterior #var auxiliar q o prof. maicris disse na sala hj
        serie = anterior
        anterior = proximo

    continuar = input("\nquer continuar?(s/n)").lower()
    if continuar == "n":
        break