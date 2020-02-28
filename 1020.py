# -*- coding: utf-8 -*-

i = int(input())
ano = i//365
meses = (i%365)//30
dias = (i%365)%30

print('{} ano(s)\n{} mes(es)\n{} dia(s)'.format(ano, meses, dias))