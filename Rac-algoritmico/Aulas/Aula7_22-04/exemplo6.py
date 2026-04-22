"""
validar as entradas de um codigo usando funções
somar 2 numeros
"""
import utils as u

num1 = u.get_int_num("Digite o primeiro numero: ")
num2 = u.get_int_num("Digite o primeiro numero: ")
soma = u.somar(num1, num2)
print("A soma dos numeros é: ", soma)