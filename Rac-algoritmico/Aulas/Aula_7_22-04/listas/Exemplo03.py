"""
Somar indefinidos números e retornar o resultado
"""
nums = []
while True:
    num = int(input("Digite um número para somar (0 para sair): "))
    if num == 0:
        break
    nums.append(num)
print(f"A soma dos números é {sum(nums)}")