# -*- coding: utf-8 -*-

ponto = input().split(' ')

if float(ponto[0]) == 0.0 and float(ponto[1]) == 0.0:
    print('Origem')
elif float(ponto[0]) == 0.0:
    print('Eixo Y')
elif float(ponto[1]) == 0.0:
    print('Eixo X')
elif float(ponto[0]) < 0 and float(ponto[1]) > 0:
    print('Q2')
elif float(ponto[0]) < 0 and float(ponto[1]) < 0:
    print('Q3')
elif float(ponto[0]) > 0 and float(ponto[1]) > 0:
    print('Q1')
else:
    print('Q4')





