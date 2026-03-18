ano = int(input("digite seu ano de nascimento:"))
calculo =  2026 - ano
calculo2 = calculo - 1
aniversariado = input("Você já fez aniversário? (s/n)").lower() == "s" # pode ser: in ("s", "sim", "yes", "y") ao invés de == "s"
if aniversariado == True:
    print (f"sua idade é: {calculo}")
else:
    print (f"sua idade é: {calculo2}")