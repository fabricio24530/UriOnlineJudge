# -*- coding: utf-8 -*-

import math

valores = input().split(' ')
a, b, c = float(valores[0]), float(valores[1]), float(valores[2])

delta = (b * b) - (4 * a * c)

if delta < 0 or a == 0:
    print('Impossivel calcular')
else:
    delta = math.sqrt(delta)
    x1 = (-b + delta) / (2 * a)
    x2 = (-b - delta) / (2 * a)
    print('R1 = {:.5f}'.format(x1))
    print('R2 = {:.5f}'.format(x2))


