# -*- coding: utf-8 -*-

nome = input()
salario = float(input())
vendas = float(input())
bonus = vendas * 0.15
total = salario + bonus
print('TOTAL = R$ {:.2f}'.format(total))


