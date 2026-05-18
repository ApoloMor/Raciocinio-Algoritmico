'''Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa
deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma
para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor A para A.M. e P para
P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua
um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.'''
def conversao(hora, minutos, A, P):
    if hora > 0 and hora < 12:
        return f'{hora}:{minutos} {A}'
    elif hora >= 12:
        if hora - 12 == 0:
            return f'{hora}:{minutos} {P}'
        else:
            return f'{hora - 12}:{minutos} {P}'
    elif hora == 0:
        return f'12:{minutos} {A}'
    
def main():
    while True:
        A = 'A.M.'
        P = 'P.M.'
        hora = int(input('Digite somente a hora: '))
        minutos = int(input('Digite os minutos: '))
        print(conversao(hora, minutos, A, P))
        if input('Deseja fazer mais conversões? (S/N) ').upper() == 'N':
            break
        
main()