n1 = int(input())
n2 = int(input())
soma = 0

if n1 > n2:
    for i in range(n2 + 1, n1):
        if i%2 != 0:
            soma = soma + i
    print(soma)
elif n1 < n2:
    for i in range(n1 + 1, n2):
        if i%2 != 0:
            soma = soma + i
    print(soma)
elif n1 == n2:
    print('0')
