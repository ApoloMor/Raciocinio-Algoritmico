def imprimir_padrao(n):
    for i in range(1, n + 1):
        linha = ""

        for j in range(1, i + 1):
            linha += str(j) + " "

        print(linha)

num = int(input("Digite um valor para n: "))
imprimir_padrao(num)