def get_int_num(msg):
    while True:
        try:
            return int(input(msg))
        except:
            print("Valor inválido!!!")
def somar(num1, num2):
    return num1 + num2