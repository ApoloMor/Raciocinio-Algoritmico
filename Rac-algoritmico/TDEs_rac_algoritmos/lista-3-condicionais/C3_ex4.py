"""
Implemente um programa que calcule o que deve ser pago por um produto,
considerando o preço normal de etiqueta e a escolha da condição de pagamento. Utilize
os códigos da tabela a seguir para ler qual a condição de pagamento escolhida e efetuar o
cálculo adequado.
Código Condição de pagamento
• 1 – À vista em dinheiro ou cheque, recebe 10% de desconto
• 2 – À vista no cartão de crédito, recebe 15% de desconto
• 3 – Em duas vezes, preço normal de etiqueta sem juros
• 4 – Em duas vezes, preço normal de etiqueta mais juros de 10%
"""
while True:
    preco_etiqueta = 600
    pay_meth = str(input("qual será o metodo de pagamento? A vista dinheiro ou cheque (V), a vista cartão de crédito (C), Duas vezes sem juros(S), duas vezes com juros (J)")).lower()
    if pay_meth == "v":
        preco_etiqueta = preco_etiqueta - (preco_etiqueta * 0.1)
    elif pay_meth == "c":
        preco_etiqueta = preco_etiqueta - (preco_etiqueta * 0.15)
    elif pay_meth == "s":
        preco_etiqueta = preco_etiqueta
    elif pay_meth == "j":
        preco_etiqueta = preco_etiqueta + (preco_etiqueta * 0.1)
    else:
        print("Entrada inválida!")
        break
    print(f"Você deve pagar {preco_etiqueta}")
