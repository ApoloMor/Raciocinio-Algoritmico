def menu():
    print("Menu")
    print("1. Cadastrar")
    print("2. Imprimir")
    print("3. Sair")

def cadastrar(dados):
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    cidade = input("Digite usa cidade: ")
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
            dados.append()