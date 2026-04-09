"""Criar um programa que solicite ao usuário vários números e, ao
digitar 0, calcula a média destes números informados.
"""
deno = -1
numera = 0
while True:
    perg = int(input("digite um número:"))
    numera += perg
    deno += 1
    if perg == 0:
        if deno != 0:
            media = numera / deno
            print(f"a media é {media}")
            deno = -1
            numera = 0
            media = 0
        else:
            print("divisão por 0 impossível")