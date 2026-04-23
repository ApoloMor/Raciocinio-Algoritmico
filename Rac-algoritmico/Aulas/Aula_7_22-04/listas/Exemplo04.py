"""
Calcular a média de vários números dados
"""
nums = []
while True:
    num = int(input("Digite um número para somar (0 para sair): "))
    if num == 0:
        break
    nums.append(num)
media = sum(nums)/len(nums)
print(f"A média dos números {nums} é {media}")