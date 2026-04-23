"""
Cadastro de Banco de Dados
"""
def menu():
    print("Menu")
    print("1. Cadastrar")
    print("2. Imprimir")
    print("3. Sair")

def cadastrar(dados):
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    cidade = input("Digite a cidade: ")
    cliente = [nome, idade, cidade]
    return cliente

def imprimir(dados):
    for dado in dados:
        print(dado)

def main():
    dados = []
    while True:
        menu()
        op = int(input("Digite uma opção: "))
        if op == 1:
            dados.append(cadastrar(dados))
        elif op == 2:
            imprimir(dados)
        elif op == 3:
            break
        else:
            print("Opção inválida!!!")

main()