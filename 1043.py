# -*- coding: utf-8 -*-

def condicao(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return print('Perimetro = {:.1f}'.format(a+b+c))
    else:
        print('Area = {:.1f}'.format(((a+b)/2)*c))

valores = input().split(' ')

condicao(float(valores[0]), float(valores[1]), float(valores[2]))