"""Um determinado material radioativo perde metade de sua massa a cada 50 segundos.
Dada a massa inicial, em gramas, fazer um algoritmo que determine o tempo necessário
para que a massa se torne menor do que 0,5 grama. Imprima como dado de saída a massa
final e o tempo calculado em segundos"""
count = 0
massa = float(input("Insira a massa do material: "))
while massa > 0.5:
    div = massa / 2
    count += 1
    if div <= 0.5:
        seg = count * 50
print(f"Massa final: {massa:.2f} g")
print(f"Tempo total: {seg} segundos")
