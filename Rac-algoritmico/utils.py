def get_int_num(msg):
    while true:
        try:
            num = int(input(msg))
            return num
        exept:
            print("Valor invaálido!!!")