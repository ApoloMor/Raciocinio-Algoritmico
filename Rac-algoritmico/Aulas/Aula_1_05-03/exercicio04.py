total = 0
while True :
    produto = input("Escolha um produto:\nLaranja - R$1.50\nBanana - R$2.00\nCaqui - R$1.00\n").lower()
    preco = float(2.30)
    preco2 = float(2.00)
    preco3 = float(1.00)
    if produto in ("laranja", "banana", "caqui"):
        quantidade = int(input("Quantos você deseja comprar?"))
        if produto == "laranja":
            total =+ quantidade * preco
        elif produto == "banana":
            total =+ quantidade * preco2
        elif produto == "caqui":
            total =+ quantidade * preco3
    pagamento = input("o pagamento será a vista? (s/n)").lower() in("s", "sim", "y", "yes")
    desconto = total - (total * 0.15)
    if pagamento == True:
        print(f"O custo total é de {desconto:.2f}")
    else:
        print(f"O custo total é de {total:.2f}")
    break