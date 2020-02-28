# -*- coding: utf-8 -*-
import math
x = input().split(' ')
y = input().split(' ')

distancia = math.sqrt(pow((float(y[0])-float(x[0])), 2) + pow((float(y[1]) - float(x[1])), 2))

print('{:.4f}'.format(distancia))