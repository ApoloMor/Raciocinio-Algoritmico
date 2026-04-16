txt = str(input("Digite uma palavra ou frase: "))
cont = 1
final = ""
anterior = ""
primeira = True
for l in txt:
  if primeira:
    anterior = l
    primeira = False
  else:
    if anterior == l:
      cont += 1
    else:
      final += anterior + str(cont)
      cont = 1
      anterior = l
final += anterior + str(cont)
print(final)