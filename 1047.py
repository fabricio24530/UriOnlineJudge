# -*- coding: utf-8 -*-

def tempo(a, b, c, d):
    conth = 0
    minutos = 0
    if a < c:
        total = abs(((a*60)+b) - ((c*60)+d))
        horas = total//60
        minutos = total%60
        return print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(horas, minutos))
    elif (a == b and b == c and c == d):
        return print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
    elif a == c and b == d:
        return print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
    elif a == c and b < d:
        horas = 0
        minutos = d - b
        return print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(horas, minutos))
    elif a == c and b > d:
        total = ((24*60) - ((a*60) + b)) + ((c*60) + d)
        horas = total//60
        minutos = total%60
        return print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(horas, minutos))
    elif a > c:
        total = ((24*60) - ((a*60) + b)) + ((c*60) + d)
        horas = total//60
        minutos = total%60
        return print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(horas, minutos))

hora_inicio, minuto_inicio, hora_fim, minuto_fim = input().split(' ')

if int(hora_inicio) >= 0 and int(hora_fim) >= 0 and int(minuto_inicio) >=0 and int(minuto_fim)>= 0:
    tempo(int(hora_inicio), int(minuto_inicio), int(hora_fim), int(minuto_fim))
