# -*- coding: utf-8 -*-

valores = input().split(' ')
a = float(valores[0])
b = float(valores[1])
c = float(valores[2])

area_triangulo = (a * c)/2
area_circulo = 3.14159 * pow(c, 2)
area_trapezio = ((a+b)*c)/2
area_quadrado = pow(b, 2)
area_retangulo = a * b

print('TRIANGULO: {:.3f}\nCIRCULO: {:.3f}\nTRAPEZIO: {:.3f}\nQUADRADO: {:.3f}\nRETANGULO: {:.3f}'.format(area_triangulo, area_circulo, area_trapezio, area_quadrado, area_retangulo))
