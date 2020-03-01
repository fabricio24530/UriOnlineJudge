# -*- coding: utf-8 -*-

def multiplos(a, b):
    if a%b == 0 or b%a == 0:
        return print('Sao Multiplos')
    else:
        return print('Nao sao Multiplos')

numeros = input().split(' ')

multiplos(int(numeros[0]), int(numeros[1]))