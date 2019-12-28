def tempo(d1, h1, m1, s1, d2, h2, m2, s2):
   



dia1 = int(input('Dia: '))
inicio_dia1 = input()


dia2 = int(input('Dia: '))
inicio_dia2 = input()

if ' : ' in inicio_dia2 and ' : ' in inicio_dia1:

    
    inicio_dia1.split(':')
    inicio_dia2.split(':')

    hora_dia_1 = inicio_dia1[0]
    minuto_dia_1 = inicio_dia1[1]
    segundo_dia_1 = inicio_dia1[2]

    hora_dia_2 = inicio_dia2[0]
    minuto_dia_2 = inicio_dia2[1]
    segundo_dia_2 = inicio_dia2[2]

    if (1 <= dia1 <= 30 and 1 <= dia2 <= 30) and (1 <= int(hora_dia_1) <= 24 and 1 <= int(hora_dia_2)) and (1 <= int(minuto_dia_1) <= 60 and 1 <= int(minuto_dia_2) <= 60 ) and (1 <= int(segundo_dia_1) <= 60 and 1 <= int(segundo_dia_2) <= 60):
        tempo(int(dia1), int(hora_dia_1), int(minuto_dia_1), int(segundo_dia_1), int(dia2), int(hora_dia_2), int(minuto_dia_2), int(segundo_dia_2))


  
