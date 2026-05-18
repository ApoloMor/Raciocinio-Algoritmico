def imprimir_padrao(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
num = int(input("Digite um valor para n: "))
imprimir_padrao(num)