def imprimir_cardapio(cardapio: dict):
    print("*" * 10, "Restaurante Boca Feliz", "*" * 10)
    for item in cardapio:
        print(item)
    print("*" * (22 + len("Restaurante Boca Feliz")))

def executar_pedido(estoque: dict, ingredientes: list):
    faltantes = verificar_estoque(estoque, ingredientes)
    if len(faltantes) == 0:
        reduzir_estoque(estoque, ingredientes)
        return True, None
    else:
        return False, faltantes

def verificar_estoque(estoque: dict, ingredientes: list):
    faltantes = []
    for ingrediente in ingredientes:
        n = ingredientes.count(ingrediente)
        if estoque[ingrediente] < n:
            faltantes.append(ingrediente)
    return faltantes

def reduzir_estoque(estoque: dict, ingredientes: list):
    for ingrediente in ingredientes:
        estoque[ingrediente] -= 1

def main():
    estoque = {'pao': 10, 'hamburguer': 2, 'tomate': 5, 'bacon': 5, 'ovo': 5}
    cardapio = {
        'x-burguer': ['pao', 'hamburguer'],
        'x-salada': ['pao', 'hamburguer', 'tomate'],
        'x-bacon': ['pao', 'hamburguer', 'tomate', 'bacon'],
        'x-egg': ['pao', 'hamburguer', 'ovo'],
        'x-tudo': ['pao', 'hamburguer', 'tomate', 'hamburguer', 'bacon', 'ovo']
    }
    while True:
        imprimir_cardapio(cardapio)
        pedido = input("O que deseja pedir (0 para sair)? ")
        if pedido == "0":
            break
        elif pedido not in cardapio:
            print("Item não localizado no cardápio")
        else:
            retorno, faltantes = executar_pedido(estoque, cardapio[pedido])
            if retorno:
                print(f"Um {pedido} saindo no capricho!!!")
            else:
                for ingrediente in faltantes:
                    print(f"Infelizmente acabou o {ingrediente}")

main()