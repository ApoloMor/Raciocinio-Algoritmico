'''
imprimir cada de um string'''
nome = input("digite seu nome: ")
primeira = True
nome_formatado = ""
for letra in nome:
    if primeira:
        nome_formatado += letra.upper()
        primeira = False
    else:
        nome_formatado += letra.lower()
print(nome_formatado)