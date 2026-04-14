peso_ideal = None
altura = float(input("Informe sua altura:"))
peso = float(input("Informe seu peso:"))
sexo = input("você é homem ou mulher?(h/m)").lower()
if sexo == "h":
    peso_ideal = (72.7 * altura) - 58
    print(f"Seu peso ideal é: {peso_ideal:.2f}")
elif sexo == "m":
    peso_ideal = (62.1 * altura) - 44.7
    print(f"Seu peso ideal é: {peso_ideal:.2f}")
else:
    print("Entrada inválida!")
