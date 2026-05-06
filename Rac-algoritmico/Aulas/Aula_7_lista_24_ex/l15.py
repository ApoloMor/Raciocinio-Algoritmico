'''Faça um programa que leia um número indeterminado de valores, correspondentes a notass, encerrando a entrada
de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados,
faça:
a. Mostre a quantidade de valores que foram lidos;
b. Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
c. Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
d. Calcule e mostre a soma dos valores;
e. Calcule e mostre a média dos valores;
f. Calcule e mostre a quantidade de valores acima da média calculada;
g. Calcule e mostre a quantidade de valores abaixo de sete;
h. Encerre o programa com uma mensagem;'''
notas = []
while True:
    questNotas = int(input('Digite a notas(-1 para encerrar): '))
    if questNotas == -1:
        break
    else:
        notas.append(questNotas)
print(f'quantidade de notas: {len(notas)}')
print(f'notas inseridas: {notas}')
print('Notas na ordem reversa: ')
for nota in reversed(notas):
    print(nota)
print(f'A soma das notas é de: {sum(notas)}')
media = 0
for nota in notas:
    media += int(nota)
media = media/len(notas)
print(f'media das notas é de: {media:.2f}')
for nota in notas:
    if nota > media:
        print(f'valor acima da media: {nota}')
    if nota < 7:
        print (f'valor menor do que 7: {nota}')
print ('Encerrando programa...')