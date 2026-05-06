'''Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
a. "Telefonou para a vítima?"
b. "Esteve no local do crime?"
c. "Mora perto da vítima?"
d. "Devia para a vítima?"
e. "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da
pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como
"Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como
"Inocente"'''
perguntas = [
    "Telefonou para a vítima? (Sim/Não) ",
    "Esteve no local do crime? (Sim/Não) ",
    "Mora perto da vítima? (Sim/Não) ",
    "Devia para a vítima? (Sim/Não) ",
    "Já trabalhou com a vítima? (Sim/Não) "]
possiveisSims = ['sim', 's']
contSim = 0
for pergunta in perguntas:
    resposta = input(pergunta).lower()
    if resposta in possiveisSims:
        contSim += 1
if contSim == 5:
    julgamento = 'Assassino'
elif contSim >= 3:
    julgamento = 'Cúmplice'
elif contSim == 2:
    julgamento = 'Suspeita'
else:
    julgamento = 'Inocente'
print(julgamento)