'''
Criar um programa que solicita ao usuário 6 números, calculando
sua média. Mostrar ao usuário uma lista com os números iguais
ou acima da média e uma lista com os números abaixo da média
'''
ig = []
dif = []
todos = []
soma = 0
for n in range(1,7):
    num = int(input(f"Digite o {n} número: "))
    soma += num
    todos += [n]
media = soma / 6
for i in todos:
    if todos[i] >= media:
        ig += [todos[i]]
    else:
        dif += [todos[i]]

print(todos, ig, dif)
