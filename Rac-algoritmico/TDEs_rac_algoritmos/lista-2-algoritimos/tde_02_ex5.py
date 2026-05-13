'''Faça um algoritmo que leia as 3 notas de um aluno e calcule a média final deste aluno.
Considerar que a média é ponderada e que o peso das notas é: 2,3 e 5, respectivamente.'''
peso1 = 2
peso2 = 3
peso3 = 5
nota1 = float(input("digite o valor da primeira nota:"))
nota2 = float(input("digite o valor da segunda nota:"))
nota3 = float(input("digite o valor da terceira nota:"))
soma_pesos = peso1 + peso2 + peso3
media = ((nota1 * peso1) + ( nota2 * peso2) + (nota3 * peso3)) / soma_pesos
print (f"Sua média final é de {media:.2f}")