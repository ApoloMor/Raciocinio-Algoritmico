'''Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de
uma conta. O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar
estes valores para a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa
que a chamou. O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá
voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a
prestação. Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade
e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para
pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de
juros por dia de atraso.'''

def valorPagamento(prestacao, diasAtraso):
    if diasAtraso == 0:
        return prestacao
    else:
        multa = prestacao * 0.03
        juros = prestacao * 0.001 * diasAtraso
        return prestacao + multa + juros
    
def main():
    contadorPrest = 0
    totalPrest = 0
    while True:
        prestacao = float(input('Insira o valor da prestação: (0 para encerrar)'))
        if prestacao == 0:
            break
        diasAtraso = int(input('Informe os dias em atraso: '))
        valorFinal = valorPagamento(prestacao, diasAtraso)
        print(f'Valor a pagar: R${valorFinal:.2f}')
        contadorPrest += 1
        totalPrest += valorFinal
    print('*' * 10, 'Relatório Do Dia', '*' * 10)
    print(f'Total de prestações pagas: {contadorPrest}')
    print(f'Valor total pago: R${totalPrest:.2f}')

main()