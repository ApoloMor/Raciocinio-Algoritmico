# PV=nRT
P = float(input ("Digite a pressão: "))
T = float(input ("Digite a temperatura: "))
n = float(input ("Digite a quantidade de mols: "))
R = 0.082
V = (n*R*T)/P
print (f"O volume é: {V:.2f} L")
if V < 10:
    print ("O volume é pequeno")
elif V>= 10 and V <= 50:
    print ("O volume é médio")   
else:
    print ("O volume é grande")