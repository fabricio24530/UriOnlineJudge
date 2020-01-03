
n = int(input())
cont_in = 0
cont_out = 0

for i in range(0, n):

    valor = int(input())

    if 10 <= valor <= 20:
        cont_in += 1
    else:
        cont_out += 1
    
print('{} in\n{} out'.format(cont_in, cont_out))
