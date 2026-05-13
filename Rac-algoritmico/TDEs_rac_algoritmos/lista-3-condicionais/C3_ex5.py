while True:    
    passagem = None
    
    destino = input("Qual seu destino?\nNorte\nNordeste\nCentro-Oeste\nSul\nSair\n").lower()
    
    if destino == "sair":
        print("Encerrando programa...")
        break

    ida_e_volta = input("ida ou ida e volta?(1/2/Sair)\n").lower()
    
    if ida_e_volta == "sair":
        print("Encerrando programa...")
        break

    if ida_e_volta == "1":
        if destino == "norte":
            passagem = 500
        elif destino == "nordeste":
            passagem = 350
        elif destino == "centro-oeste" or destino == "centro oeste":
            passagem = 350
        elif destino == "sul":
            passagem = 300

    elif ida_e_volta == "2":
        if destino == "norte":
            passagem = 900
        elif destino == "nordeste":
            passagem = 650
        elif destino == "centro-oeste" or destino == "centro oeste":
            passagem = 600
        elif destino == "sul":
            passagem = 550

    if passagem is None:
        print("Entrada inválida")
    else:
        print(f"O custo da passagem é de R${passagem}")