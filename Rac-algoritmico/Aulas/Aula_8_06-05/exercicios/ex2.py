'''Criar um programa que cadastre funcionário de um empresa e
seus dependentes. O funcionário deve ser cadastrado com
matrícula, nome e dependentes. Os dependentes devem ser
inseridos dinamicamente em uma tupla. Dica: usar o operador +=.'''
funcionarios = []
while True:
    matricula = input('Digite sua matricula: ')
    nome = input('Digite seu nome: ')
    dependentes = ()
    while True:
        dependente = input('Informe um dependente (ou "fim" para parar): ')
        if dependente.lower() == 'fim':
            break
        dependentes += (dependente,)
    funcionario=(matricula, nome, dependentes)
    funcionarios.append(funcionario)
    continuar = input("Deseja cadastrar outro funcionario? (s/n): ").lower()
    if continuar != 's':
        break
print("Lista de funcionarios cadastrados:")
for f in funcionarios:
    print(f)