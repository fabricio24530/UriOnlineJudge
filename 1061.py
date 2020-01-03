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

    if total >= 60:
        return print('{} dia(s)\n{} hora(s)\n{} minuto(s)\n{} segundo(s)'.format(dias, horas, minutos, segundos))
    else:
        pass
    
dia1 = input().capitalize().strip().split(' ')
horario1 = input().strip().replace(' ', '').split(':')
dia2 = input().capitalize().strip().split(' ')
horario2 = input().strip().replace(' ', '').split(':')

tempo(int(dia1[1]), int(horario1[0]), int(horario1[1]), int(horario1[2]), int(dia2[1]), int(horario2[0]), int(horario2[1]), int(horario2[2]))

