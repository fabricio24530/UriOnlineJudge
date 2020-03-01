# -*- coding: utf-8 -*-

def ddd(a):

    dicionario = {
    61: 'Brasilia',
    71: 'Salvador',
    11: 'Sao Paulo',
    21: 'Rio de Janeiro',
    32: 'Juiz de Fora',
    19: 'Campinas',
    27: 'Vitoria',
    31: 'Belo Horizonte'}
    if a in dicionario:
        return print(dicionario[a])
    else:
        return print('DDD nao cadastrado')

num = int(input())

ddd(num)