from collections import namedtuple
#typename define o tipo /// field name define os "indices" /// não precisa escrever eles
Pessoa = namedtuple(typename="Pessoa", field_names=["nome", 'idade', 'cidade'])
maicris = Pessoa(nome = "Maicris", idade = 49, cidade = "Curitiba")
print(maicris.nome)
print(maicris.idade)
print(maicris.cidade)
#funciona como o indice, porem é mais visual e pratico