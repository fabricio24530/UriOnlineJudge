# -*- coding: utf-8 -*-

def tempo(a, b):
    cont = 0
    cont2 = 0
    if a < b:
        for i in range(a, b):
            cont += 1
        print('O JOGO DUROU {} HORA(S)'.format(cont))
    elif a > b:
        for i in range(0, (24-a) + b):
            cont2 += 1
        print('O JOGO DUROU {} HORA(S)'.format(cont2))
    elif a == b:
        print('O JOGO DUROU 24 HORA(S)')


inicio, fim = input().split(' ')

if int(inicio) >= 0 and int(fim) >= 0:
    tempo(int(inicio), int(fim))

