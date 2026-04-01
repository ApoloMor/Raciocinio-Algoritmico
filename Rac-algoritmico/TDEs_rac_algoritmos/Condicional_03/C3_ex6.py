while True:
    A = float(input("Valor de A:"))
    B = float(input("Valor de B:"))
    C = float(input("Valor de C:"))
    
    delta = B**2 -4*A*C
    
    if delta < 0 or A == 0: #validação dos valores
        msg = "Inconsistência: Delta negativo ou A inválido"
        print(msg)
    else:
        x1 = (-B + delta ** 0.5)/(2*A)
        x2 = (-B - delta ** 0.5)/(2*A)
        msg =f"Os possiveis reultados são:x1 = {x1:.3} e x2 = {x2:.3}"
        print(msg)
    if input("Deseja continuar? (s/n): ").lower() == "n":
        print("Encerrando...")
        break