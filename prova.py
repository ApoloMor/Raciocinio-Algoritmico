txt = str(input("Digite uma palavra ou frase"))
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
      final += l + str(cont)
    else:
      final += l + "1"
      cont = 0
print(final)
