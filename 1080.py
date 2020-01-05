
lista = [] 

for i in range(0, 100):
    aux = int(input())
    if (aux > 0):
        lista.append(aux)
    else:
        pass

print(max(lista))  
print(lista.index(max(lista)) + 1)
