'''Um sistema de equações lineares do tipo: ax + by = c -- dx + ey = f
pode ser resolvido da seguinte maneira:
x = (ce - bf) / (ae - bd)
y = (af - cd) / (ae - bd)
'''
a = float(input("digite o valor de a:"))
b = float(input("digite o valor de b:"))
c = float(input("digite o valor de c:"))
d = float(input("digite o valor de d:"))
e = float(input("digite o valor de e:"))
f = float(input("digite o valor de f:"))

denominador = (a*e - b*d)
if denominador == 0:
    print("O sistema não possui solução única.")
else:
    x = (e*c - b*f) / denominador
    y = (a*f - c*d) / denominador
    print(f"Os valores de x e y são, respectivamente: {x:.2f} e {y:.2f}")