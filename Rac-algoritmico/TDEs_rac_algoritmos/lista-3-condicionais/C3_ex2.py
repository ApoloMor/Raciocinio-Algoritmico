'''IMC = peso / altura2. Implemente um programa que leia o peso e a altura de um adulto e mostre
sua condição de acordo com a tabela abaixo.
IMC em adultos Condição
• Abaixo de 18,5 – Abaixo do peso
• Entre 18,5 e 25 – Peso normal
• Entre 25 e 30 – Acima do peso
• Acima de 30 – Obeso'''

peso = float(input("Qual o seu peso?"))
altura = float(input("Qual a sua altura?"))
imc = peso / (altura **2)
if imc < 18.5:
    msg = ("Você está abaixo do peso normal")
elif imc <= 25:
    msg = ("Você está dentro do peso normal")
elif imc < 30: 
    msg = ("Você está acima do peso normal")
else: 
    msg = ("Você está obeso")

print(msg)