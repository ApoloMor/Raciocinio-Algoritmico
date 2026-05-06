"""dicionarios e chaves"""
dicResp = {True:"Pode dirigir", False: "Não pode dirigir"}
idade = int(input('Digite sua idade: '))
print(dicResp(idade>=18))
