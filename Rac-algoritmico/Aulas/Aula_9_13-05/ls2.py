def fatorial(num):
    resultado = 1
    for n in range(1, num + 1):
        resultado *= n
    return resultado
num = int(input('digite um numero: '))
fat = fatorial(num)
print(fat)