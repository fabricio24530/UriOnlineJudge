# -*- coding: utf-8 -*-

valores = input().split(' ')
a = int(valores[0])
b = int(valores[1])
c = int(valores[2])

maior = (a + b + (abs(a - b)))/2

if c > maior:
    print('{} eh o maior'.format(c))
else:
    print('{} eh o maior'.format(int(maior)))