'''Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as
consoantes'''
consoantes = ['a', 'e', 'i', 'o', 'u']
cont = 0
aux = []
while True:
    word = input("Digite a palavra/frase (1-10 caracteres): ")
    if len(word) > 10 or len(word) < 1:
        print("Digite dentro do limite! (1-10 caracteres)")
    else:
        for c in word:
            if c in consoantes:
                cont += 1
                aux += [c]
        break
print(f"Foram lidas {cont} consoantes, sendo elas: {aux} ")    
