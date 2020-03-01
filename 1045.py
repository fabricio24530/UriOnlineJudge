# -*- coding: utf-8 -*-


def triangulo(a, b, c):
    if a >= b + c:
        return print('NAO FORMA TRIANGULO')
    elif a**2 == b**2 + c**2 and ((a == b and b != c) or (a == c and c != b) or (b == c and c != a)):
        return print('TRIANGULO RETANGULO\nTRIANGULO ISOSCELES')
    elif a**2 == b**2 + c**2 and ((a == b and b == c) or (c == a and a == b)):
        return print('TRIANGULO RETANGULO\nTRIANGULO EQUILATERO')
    elif a**2 == b**2 + c**2:
        return print('TRIANGULO RETANGULO')
    elif a**2 > b**2 + c**2 and ((a == b and b == c) or (c == a and a == b)):
        return print('TRIANGULO OBTUSANGULO\nTRIANGULO EQUILATERO')
    elif a**2 > b**2 + c**2 and ((a == b and b != c) or (a == c and c != b) or (b == c and c != a)):
        return print('TRIANGULO OBTUSANGULO\nTRIANGULO ISOSCELES')
    elif a**2 > b**2 + c**2:
        return print('TRIANGULO OBTUSANGULO')
    elif a**2 < b**2 + c**2 and ((a == b and b == c) or (c == a and a == b)):
        return print('TRIANGULO ACUTANGULO\nTRIANGULO EQUILATERO')
    elif a**2 < b**2 + c**2 and ((a == b and b != c) or (a == c and c != b) or (b == c and c != a)):
        return print('TRIANGULO ACUTANGULO\nTRIANGULO ISOSCELES')
    elif a**2 < b**2 + c**2:
        return print('TRIANGULO ACUTANGULO')

valores = input().split(' ')

if float(valores[0]) > 0 and float(valores[1]) > 0 and float(valores[2]) > 0:
    lista = [float(valores[0]), float(valores[1]), float(valores[2])]
    lista.sort(reverse=True)
    triangulo(float(lista[0]), float(lista[1]), float(lista[2]))
