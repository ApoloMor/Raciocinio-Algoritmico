'''
soma n numeros pares
range(stop)
range(start, stop)
range(start, stop, step)
'''
n = int(input("quantos numeros deseja somar?"))
soma = 0
for num in range(0, 2*n, 2):
        soma += num
print(f"a soma dos {n} primeiros numeros pares é {soma}")