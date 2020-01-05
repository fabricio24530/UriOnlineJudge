# -*- coding: utf-8 -*-

valor = int(input())

cedula_100 = valor // 100
cedula_50 = (valor % 100) // 50
cedula_20 = ((valor % 100) % 50)//20
cedula_10 = (((valor % 100) % 50)%20)//10
cedula_5 = ((((valor % 100) % 50)%20)%10)//5
cedula_2 = (((((valor % 100) % 50)%20)%10)%5)//2
cedula_1 = ((((((valor % 100) % 50)%20)%10)%5)%2)//1

print('{}\n{} nota(s) de R$ 100,00\n{} nota(s) de R$ 50,00\n{} nota(s) de R$ 20,00'.format(valor, cedula_100, cedula_50, cedula_20))
print('{} nota(s) de R$ 10,00\n{} nota(s) de R$ 5,00\n{} nota(s) de R$ 2,00\n{} nota(s) de R$ 1,00'.format(cedula_10, cedula_5, cedula_2, cedula_1))
   

