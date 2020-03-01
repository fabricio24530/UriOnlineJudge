# -*- coding: utf-8 -*-

def reajuste(a):
    if a >= 0 and a <= 400:
        reajuste = a * 0.15
        novo_salario = a + reajuste
        return print('Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: 15 %'.format(novo_salario, reajuste))
    elif a >= 400.01 and a <= 800:
        reajuste = a * 0.12
        novo_salario = a + reajuste
        return print('Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: 12 %'.format(novo_salario, reajuste))
    elif a >= 800.01 and a <= 1200:
        reajuste = a * 0.10
        novo_salario = a + reajuste
        return print('Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: 10 %'.format(novo_salario, reajuste))
    elif a >= 1200.01 and a <= 2000:
        reajuste = a * 0.07
        novo_salario = a + reajuste
        return print('Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: 7 %'.format(novo_salario, reajuste))
    else:
        reajuste = a * 0.04
        novo_salario = a + reajuste
        return print('Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: 4 %'.format(novo_salario, reajuste))

entrada = float(input())

if entrada >= 0:
    reajuste(entrada)



