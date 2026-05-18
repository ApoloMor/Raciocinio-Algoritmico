def imprimir_padrao(n):
    for i in range(1, n + 1):
        linha = (str(i) + " ") * i
        print(linha.strip())
num = int(input("Digite um valor para n: "))
imprimir_padrao(num)
