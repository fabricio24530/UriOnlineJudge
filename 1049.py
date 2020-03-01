# -*- coding: utf-8 -*-

def animal(a, b, c):
    if a == 'vertebrado' and b == 'ave' and c == 'carnivoro':
        return print('aguia')
    elif a == 'vertebrado' and b == 'ave' and c == 'onivoro':
        return print('pomba')
    elif a == 'vertebrado' and b == 'mamifero' and c == 'onivoro':
        return print('homem')
    elif a == 'vertebrado' and b == 'mamifero' and c == 'herbivoro':
        return print('vaca')
    elif a == 'invertebrado' and b == 'inseto' and c == 'hematofago':
        return print('pulga')
    elif a == 'invertebrado' and b == 'inseto' and c == 'herbivoro':
        return print('lagarta')
    elif a == 'invertebrado' and b == 'anelideo' and c == 'hematofago':
        return print('sanguessuga')
    elif a == 'invertebrado' and b == 'anelideo' and c == 'onivoro':
        return print('minhoca')

nome1 = input().lower()
nome2 = input().lower()
nome3 = input().lower()

lista0 = ['vertebrado', 'invertebrado']
lista1 = ['ave', 'mamifero', 'inseto', 'anelideo']
lista2 = ['carnivoro', 'onivoro', 'herbivoro', 'hematofago']


if (nome1 in lista0) and (nome2 in lista1) and (nome3 in lista2):
    animal(nome1, nome2, nome3)
