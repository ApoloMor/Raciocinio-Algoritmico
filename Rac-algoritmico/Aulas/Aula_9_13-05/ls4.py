'''Criar um programa que, fazendo uso de funções, cadastra contatos 
em uma agenda telefônica, podendo excluir estes contatos.
Deve ser exibido um menu com as opções: inserir, remover e sair.'''

agendaTelefonica = []

def main():
    while True:
        if input('Deseja prosseguir ou sair? (P/S) ').upper() == 'S':
            print('Encerrando programa...')
            break
        if input('Deseja adicionar um contato ou remover? (A/R) ').upper() == 'A':
            nome = input('Digite seu nome: ')
            telefone = int(input('Digite seu número: '))
            inserir(agendaTelefonica, nome, telefone)
            print(agendaTelefonica)
        else:
            print(agendaTelefonica)
            remove = int(input('Escolha por índice qual contato remover: '))
            remover(agendaTelefonica, remove)
            print(agendaTelefonica)

def inserir(agendaTelefonica, nome, telefone='sem telefone'):
    agendaTelefonica.append([nome, telefone])

def remover(agendaTelefonica, remove):
    agendaTelefonica.pop(remove)

main()