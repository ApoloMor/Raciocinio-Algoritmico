"""Criar um programa que pede para o usuário inserir um login e uma
senha. Caso os valores sejam iguais, informar que os dados são
inválidos e pedir novamente as informações. Caso contrário, exibir a
mensagem "Bem-vindo ao sistema!!!".
"""
Clog = input("Crie um login: ")
Cpwd = input("Crie uma senha: ")
while True:
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")
    if login == Clog and senha == Cpwd:
        print("Bem-vindo ao sistema!!!")
        break
    else:
        print("Login ou senha inválidos!!!")
        continue