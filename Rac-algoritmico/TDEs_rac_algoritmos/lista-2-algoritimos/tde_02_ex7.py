'''O custo ao consumidor de um carro novo é a soma do custo de fábrica com a
percentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que
a percentagem do distribuidor seja de 28% e os impostos de 45%, escrever um algoritmo
que leia o custo de fábrica de um carro e escreva o custo ao consumidor. 17600.00'''

custo_fabrica = float(input("Digite o valor de fabricação do carro:"))
imposto = custo_fabrica * 0.45
distribuicao = custo_fabrica * 0.28
valor_consumidor = custo_fabrica + imposto + distribuicao
print(f"o valor que o consumidor pagará é de {valor_consumidor:.2f}")


