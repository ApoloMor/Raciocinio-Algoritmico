#dado um nome completo separe apenas o primeiro nome
nome = input('Digite seu nome completo:')
pri_nome = ""
for i in nome:
    if i != " ":
        pri_nome += i
    else:
        break
print(f"Seu primeiro nome é: {pri_nome}")