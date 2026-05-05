'''Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor.
Imprima a idade e a altura na ordem inversa a ordem lida.'''
pessoas = []
idade = []
altura = []
for pessoa in range(1,6):
    nome = input("Digite a seu nome: ")
    pessoas.append(nome)
    questIdade = int(input("Digite a sua idade: "))
    idade.append(questIdade) 
    questAltura = float(input("Digite a sua altura: "))
    altura.append(questAltura) 
print(pessoas, idade, altura)