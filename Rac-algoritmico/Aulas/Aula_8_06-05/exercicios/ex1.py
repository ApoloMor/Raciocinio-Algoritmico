'''Criar um programa que efetua o cadastro de pessoas com nome,
rg e cpf por meio de tuplas, adicionando elas a uma lista.
Imprimir a lista ao final do programa'''
pessoas = []
while True:
    nome = input("Digite seu nome: ")
    rg = input("Digite seu RG: ")
    cpf = input("Digite seu CPF: ")
    pessoa = (nome, rg, cpf)  # tupla
    pessoas.append(pessoa)
    continuar = input("Deseja cadastrar outra pessoa? (s/n): ").lower()
    if continuar != 's':
        break
print("\nLista de pessoas cadastradas:")
for p in pessoas:
    print(p)