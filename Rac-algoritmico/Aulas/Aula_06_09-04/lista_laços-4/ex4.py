num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
num3 = int(input("Digite um número: "))
num4 = int(input("Digite um número: "))
num5 = int(input("Digite um número: "))

# laço para repetir as comparações
for _ in range(5):
    if num1 > num2:
        num1, num2 = num2, num1

    if num2 > num3:
        num2, num3 = num3, num2

    if num3 > num4:
        num3, num4 = num4, num3

    if num4 > num5:
        num4, num5 = num5, num4

print("Ordem crescente:")
print(num1, num2, num3, num4, num5)