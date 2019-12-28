# -*- coding: utf-8 -*-

def irpf(a):
    if a >= 0.0 and a <= 2000.00:
        return print('Isento')
    elif a >= 2000.01 and a <= 3000.00:
        valor = (a - 2000.00) * 0.08
        return print('R$ {:.2f}'.format(valor))
    elif a >= 3000.01 and a <= 4500.00:
        valor1 = ((a - 2000) - 1000) 
        valor2 = (a - 2000) - valor1
        juros = (valor1 * 0.18) + (valor2 * 0.08)
        return print('R$ {:.2f}'.format(juros))
    elif a > 4500.00:
        valor1 = ((a - 2000.00) - 2500.00) 
        valor2 = ((a - 2000.00) - 1000.00) - valor1
        valor3 = ((a - 2000.00)  - 1500.00) - valor1
        juros = (valor1 * 0.28) + (valor2 * 0.18) + (valor3 * 0.08)
        return print('R$ {:.2f}'.format(juros))

salario = float(input())

if salario >= 0.0:
    irpf(salario)

