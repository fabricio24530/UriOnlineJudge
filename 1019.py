# -*- coding: utf-8 -*-

N = int(input())

hora = N//3600
minutos = (N%3600)//60
segundos = (N%3600)%60

print('{}:{}:{}'.format(hora, minutos, segundos))
