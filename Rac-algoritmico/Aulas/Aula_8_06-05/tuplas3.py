'''Calculo de bhaskara'''
delta = float()
def bhaskara(a,b,c):
    if delta < 0:
        return None, None
    elif delta == 0:
        return -b/2*a, None
    else:
        x1 = (-b+ delta **0.5)/2*a
        x2 = (-b- delta **0.5)/2*a
        return x1, x2
r1, r2 = bhaskara(1, 2, 3)# em ordem define: a: 1  b:2  c: 3
#inverte r1, r2 = r2, r1