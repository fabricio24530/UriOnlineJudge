# -*- coding: utf-8 -*-

def sort(a, b, c):
     lista = [a, b, c]
     lista.sort()
     return print('{}\n{}\n{}\n'.format(lista[0], lista[1], lista[2]))

num = input().split(' ')

sort(int(num[0]), int(num[1]), int(num[2]))
print('{}\n{}\n{}'.format(num[0], num[1], num[2]))