cont_par = 0
cont_impar = 0
cont_positivo = 0
cont_negativo = 0
lista = []

for i in range(0, 5):
    valor = int(input())
    lista.append(valor)
    if valor%2 == 0:
        cont_par += 1
    elif valor%2 != 0:
        cont_impar += 1
for i in range(0, 5):
    if lista[i] > 0:
        cont_positivo += 1
    elif lista[i] < 0:
        cont_negativo += 1

print('{} valor(es) par(es)\n{} valor(es) impar(es)\n{} valor(es) positivo(s)\n{} valor(es) negativo(s)'.format(cont_par, cont_impar, cont_positivo, cont_negativo))
