#Recursividade em funções:
def somar_ant(n):
    if n == 1:
        return 1
    return n + somar_ant(n-1)
    
n = int(input('Digite um numero: '))
soma = somar_ant(n)
print(f'A soma dos antecessores de {n} é: {soma}')
