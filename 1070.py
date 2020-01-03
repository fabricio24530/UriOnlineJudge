valor = int(input())
lista = []

while (len(lista) < 6):
    for i in range(valor, valor+12):
        if i%2 != 0:
            lista.append(i)
            print(i)
