'''mutabilidade de tuplas'''
maicris = ("Maicris", 49, "Curitiba")
print(maicris)
maicris += (["joao","rafa"],)#tem q ter a virgula dps para ser tupla e poder ser adicionada
print(id(maicris))
maicris[3].append("maria")
print(id(maicris))
#maicris[0]="Maria"     não funfa pois tuplas ào imutaveis