
n = int(input())
lista = []

if n < 10000:
    for i in range(0, n):
        valor = int(input())
        lista.append(valor)
    for i in range(0, n):
        if pow(-10, 7) < lista[i] < pow(10, 7):
            if lista[i]%2 == 0 and lista[i] > 0:
                print('EVEN POSITIVE')
            elif lista[i]%2 == 0 and lista[i] < 0:
                print('EVEN NEGATIVE')
            elif lista[i]%2 != 0 and lista[i] > 0:
                print('ODD POSITIVE')
            elif lista[i]%2 != 0 and lista[i] < 0:
                 print('ODD NEGATIVE')
            elif lista[i] == 0:
                print('NULL')    
else:
    pass

    












   
