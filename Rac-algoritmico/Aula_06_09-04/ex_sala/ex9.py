"""Criar um programa que simula um carrinho de compras, onde
solicita o nome do produto (não pode ser vazio), o valor deste
produto (valor com vírgula, positivo) e a quantidade deste
produto a ser comprada (valor inteiro, positivo). Ao incluir um
produto, deve perguntar se o usuário deseja fechar o pedido ou
incluir mais produtos. Todos os dados devem ser validados. Ao
final da compra, deve ser informado o valor total do pedido.
"""
carrinho = ""
valor_total = 0

while True:
    # produtp
    while True:
        produto = input("Nome do produto: ").strip()
        if produto != "":
            break
        print("Nome não pode ser vazio!")
    # valor
    while True:
        try:
            valor = float(input("Valor do produto: ").replace(",", "."))
            if valor > 0:
                break
            else:
                print("O valor deve ser positivo!")
        except ValueError:
            print("Digite um valor válido!")
    # quantidade
    while True:
        try:
            quantidade = int(input("Quantidade: "))
            if quantidade > 0:
                break
            else:
                print("A quantidade deve ser positiva!")
        except ValueError:
            print("Digite um número inteiro válido!")
    #carrinho
    carrinho += f"{produto} ({quantidade}x), "
    valor_total += valor * quantidade
    opcao = input("Deseja adicionar mais produtos? (s/n): ").lower()
    if opcao == "n":
        carrinho = carrinho.rstrip(", ")
        print (f"o carrinho custou: {valor_total}")
        break