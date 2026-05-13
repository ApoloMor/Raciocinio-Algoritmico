'''- Imprimir a lista de unidades de conversão
- Solicitar o valor que se deseja converter usando a frase “Valor a ser convertido: ”
- Solicitar a unidade origem do valor usando a frase “Converter de: ”
- Solicitar a unidade destino de conversão usando a franse “Converter para: ”
- Exibir o valor convertido com a frase “Conversão: {valor} {unidade origem} = {valor}
{unidade destino}”'''

def main():
    ano_luz = {"pc": 0.31, "al": 1, "ae": 63241.09, "ml": 525960.23, "sl": 31557609.92}
    unidades = ["Parsec (pc)", "Ano-Luz (al)", "Unidade Astronômica (ae)", "Minuto-Luz(ml)", "Segundo-Luz (sl)"]
    while True:
        imprimir_unit(unidades, ano_luz)
        valor = float(input('Valor a ser convertido: '))
        valor_origem = input('Converter de: ')
        valor_destino = input('Converter para: ')
        resultado = conversao(ano_luz, valor, valor_origem, valor_destino)
        print(f"Conversão: {valor} {valor_origem} = {resultado:.2f} {valor_destino}")

def imprimir_unit(unidades: list, ano_luz: dict):
    print("*" * 10, "Frota Alfa", "*" * 10)
    for unit in unidades:
        print(unit)
    for chave, valor in ano_luz.items():
        print(f"{chave}: {valor}")
    print("*" * (22 + len("Frota Alfa")))

def conversao(ano_luz, valor, valor_origem, valor_destino):
    valor_em_al = valor / ano_luz[valor_origem]
    valor_convertido = valor_em_al * ano_luz[valor_destino]
    return valor_convertido

main()