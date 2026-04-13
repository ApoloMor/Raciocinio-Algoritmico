pais1 = int(5000000)
pais2 = int(7000000)
contador = 0

while pais1 < pais2:
    pais1 += int(pais1 * 0.03)
    pais2 += int(pais2 * 0.02)
    contador += 1
    print(contador, pais1, pais2)

print(f"O pais1 superou a população do pais 2 em {contador} anos!")
