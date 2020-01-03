
lista_valores_positivos = []

cont = 0
somatorio = 0

for i in range(0, 6):
    valor = input().strip().replace(' ', '')
    if '.' not in valor and int(valor) > 0:
        lista_valores_positivos.append(int(valor))
        cont += 1
        somatorio = somatorio + int(valor)
    elif '.' in valor and float(valor) > 0:
        lista_valores_positivos.append(float(valor))
        cont += 1
        somatorio = somatorio + float(valor)

if len(lista_valores_positivos) > 0:
    media = somatorio / len(lista_valores_positivos)
    print('{} valores positivos\n{:.1f}'.format(cont, media))
else:
    pass
