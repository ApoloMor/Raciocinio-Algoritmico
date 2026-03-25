'''Faça um algoritmo que leia o tempo de duração de um evento em uma fábrica
expressa em segundos e mostre-o expresso em horas, minutos e segundos.'''
tempo_segundos = int(input("Digite o tempo de duração do evento em segundos:"))
tempo_horas = tempo_segundos / 3600
resto_horas = tempo_segundos % 3600
tempo_minutos = resto_horas / 60
resto_minutos = tempo_minutos % 60
print(f"O tempo de duração do evento é: {tempo_horas} hora(s), {tempo_minutos} minuto(s) e {resto_minutos} segundo(s).")