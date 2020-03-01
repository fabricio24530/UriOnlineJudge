# -*- coding: utf-8 -*-

N = float(input())
if N >= 0 and N <= 1000000.00:
    NN = str(N).split('.')

    valor = int(NN[0])

    cedula_100 = valor // 100
    cedula_50 = (valor % 100) // 50
    cedula_20 = ((valor % 100) % 50) // 20
    cedula_10 = (((valor % 100) % 50) % 20) // 10
    cedula_5 = ((((valor % 100) % 50) % 20) % 10) // 5
    cedula_2 = (((((valor % 100) % 50) % 20) % 10) % 5) // 2

    valor2 = (int(NN[1]) / 100 + ((((((valor % 100) % 50) % 20) % 10) % 5) % 2)) + 0.0001

    moeda_1 = valor2 // 1
    moeda_05 = (valor2 % 1) // 0.5
    moeda_025 = ((valor2 % 1) % 0.5) // 0.25
    moeda_010 = (((valor2 % 1) % 0.5) % 0.25) // 0.10
    moeda_005 = ((((valor2 % 1) % 0.5) % 0.25) % 0.10) // 0.05
    moeda_001 = int((((((valor2 % 1) % 0.5) % 0.25) % 0.10) % 0.05) * 100)

    print(
        'NOTAS:\n{} nota(s) de R$ 100.00\n{} nota(s) de R$ 50.00\n{} nota(s) de R$ 20.00'.format(cedula_100, cedula_50,
                                                                                                 cedula_20))
    print('{} nota(s) de R$ 10.00\n{} nota(s) de R$ 5.00\n{} nota(s) de R$ 2.00'.format(cedula_10, cedula_5, cedula_2))

    print('MOEDAS:\n{} moeda(s) de R$ 1.00'.format(int(moeda_1)))
    print('{} moeda(s) de R$ 0.50'.format(int(moeda_05)))
    print('{} moeda(s) de R$ 0.25'.format(int(moeda_025)))
    print('{} moeda(s) de R$ 0.10'.format(int(moeda_010)))
    print('{} moeda(s) de R$ 0.05'.format(int(moeda_005)))
    print('{} moeda(s) de R$ 0.01'.format(moeda_001))

