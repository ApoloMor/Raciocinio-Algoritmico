#criar um função qe resolva bhaskara
def calc_delta(a, b, c):
    return b** 2 - 4 * a *c
    
def calc_raiz(delta, a, b):
    return (-b + delta) / (2*a)

def bhaskara (a,b,c):
    delta = calc_delta(a, b, c)
    if delta < 0:
        r1 = None
        r2 = None
    elif delta == 0:
        r1 = calc_raiz(delta, a, b)
        r2 = None
    else: 
        r1 = calc_raiz(delta, b, a)
        r2 = calc_raiz(-delta, a, b)
    return r1, r2

r1, r2 = bhaskara (a:1, b:3, c:1)
if not r1:
    print("Raizes imaginárias!")
elif not r2:
    print(f"Uma unica raiz: {r1}")
else:
    print(f"Duas raizes reais: {r1} e {r2}")


