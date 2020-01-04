number = int(input())
medias =[]

for i in range(0, number):
    notas = input().strip().split(' ')
    calculo = (float(notas[0]) * 2 + float(notas[1]) * 3 + float(notas[2]) * 5)/10
    medias.append(calculo)

for i in range(0, number):
    print('{:.1f}'.format(medias[i]))
