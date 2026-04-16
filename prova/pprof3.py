cons = int(input ("Digite o consumo: "))
valor = 5
if cons>200:
    valor += (cons -200)*0.9
    cons = 200
if cons > 100:
    valor += (cons -100)*0.75
    cons = 100
valor += cons*0.6
print (f"Valor a pagar: R$ {valor:.2f}")

#OU
cons = int(input ("Digite o consumo: "))
valor = 5
if cons <= 100:
    valor += cons*0.6
elif cons <= 200:
    valor += 100*0.6 + (cons -100)*0.75
else:
    valor += 100*0.6 + 100*0.75 + (cons -200)*0.9
print (f"Valor a pagar: R$ {valor:.2f}")