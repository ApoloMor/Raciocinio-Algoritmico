'''dicionarios cadastro de livros'''
print("Sistema de biblioteca")
livros = {}
livros['123456789'] = {'titulo': 'Pequeno principe', 'editora': 'makron'}
livros['987654321'] = {'titulo': 'O nome da Rosa', 'editora': 'Elseve'}
print(livros)
livro = input('Digite o ISBN do livro')
if livro in livros:
    print(livros[livro])
else:
    print('Livro desconhecido!')
var = []