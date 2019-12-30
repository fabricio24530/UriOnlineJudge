def tempo(d1, h1, m1, s1, d2, h2, m2, s2):
    total_dia = (d2 - d1) * 86400
    total_horas = (h2 - h1) * 3600
    total_minutos = (m2 - m1) * 60
    total_segundos = s2 - s1
    total = total_dia + total_horas + total_minutos + total_segundos
    dias = total // 86400
    horas = (total % 86400)//3600
    minutos = ((total % 86400)%3600)//60
    segundos = ((total % 86400)%3600)%60

    return print('{} dia(s)\n{} hora(s)\n{} minuto(s)\n{} segundo(s)'.format(dias, horas, minutos, segundos))
    
   
dia1 = int(input('Dia: '))
inicio_dia1 = input().split(':')

dia2 = int(input('Dia: '))
inicio_dia2 = input().split(':')

for i in range(0, 3):
    inicio_dia1[i] = inicio_dia1[i].strip()
    inicio_dia2[i] = inicio_dia2[i].strip()

hora_dia_1 = inicio_dia1[0]
minuto_dia_1 = inicio_dia1[1]
segundo_dia_1 = inicio_dia1[2]

hora_dia_2 = inicio_dia2[0]
minuto_dia_2 = inicio_dia2[1]
segundo_dia_2 = inicio_dia2[2]

if (1 <= int(dia1) <= 30 and 1 <= int(dia2) <= 30) and (1 <= int(hora_dia_1) <= 24 and 1 <= int(hora_dia_2) <= 24) and (1 <= int(minuto_dia_1) <= 60 and 1 <= int(minuto_dia_2) <= 60 ) and (1 <= int(segundo_dia_1) <= 60 and 1 <= int(segundo_dia_2) <= 60):
    tempo(int(dia1), int(hora_dia_1), int(minuto_dia_1), int(segundo_dia_1), int(dia2), int(hora_dia_2), int(minuto_dia_2), int(segundo_dia_2))


  
