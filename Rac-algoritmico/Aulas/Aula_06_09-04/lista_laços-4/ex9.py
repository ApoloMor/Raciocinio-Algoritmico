'''Elaborar um programa em Python que converta um número decimal em hexadecimal, fazendo uso do método de divisões sucessivas.
Para converter um número decimal para hexadecimal, divida sucessivamente o número decimal por 16,
anotando o resto de cada divisão, até que o quociente seja zero. Os restos, lidos da última divisão para a primeira 
(ordem inversa), formam o número hexadecimal, substituindo valores de 10 a 15 por A a F. '''
decimal = int(input("Digite um numero em decimal: "))
if decimal == 0:
    hexadecimal = "0"
else:
    hexadecimal = ""
    while decimal > 0:
        resto_divisão = decimal % 16
        if resto_divisão == 10:
            hexadecimal = 'A' + hexadecimal
        elif resto_divisão == 11:
            hexadecimal = 'B' + hexadecimal
        elif resto_divisão == 12:
            hexadecimal = 'C' + hexadecimal
        elif resto_divisão == 13:
            hexadecimal = 'D' + hexadecimal
        elif resto_divisão == 14:
            hexadecimal = 'E' + hexadecimal
        elif resto_divisão == 15:
            hexadecimal = 'F' + hexadecimal
        else:
            hexadecimal = str(resto_divisão) + hexadecimal
        decimal = decimal // 16
print("O número em hexadecimal é:", hexadecimal)