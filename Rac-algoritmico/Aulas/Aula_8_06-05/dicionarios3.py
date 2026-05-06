'''dicionarios e chaves'''
maicris= {'nome': 'Maicris', 'idade': 49, 'cidade': 'Curitiba'}
maicris['cpf'] = '00000000000'
'''if 'idade' in maicris:
    del(maicris['idade'])'''
for chave in maicris: #maicris.keys
    print(chave)
for valor in maicris.values():
    print(valor)
for chave, valor in maicris.items():
    print(valor)