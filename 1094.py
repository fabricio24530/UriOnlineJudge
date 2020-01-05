n = int(input())
total_coelho = 0
total_rato = 0
total_sapo = 0
total = 0

for i in range(0, n):
    valores = input().strip().upper().split(' ')
    total = total + int(valores[0])

    if valores[1] == 'R':
        total_rato = total_rato + int(valores[0])
    elif valores[1] == 'C':
        total_coelho = total_coelho + int(valores[0])
    elif valores[1] == 'S':
        total_sapo = total_sapo + int(valores[0])

porcentagem_rato = (total_rato/total)*100
porcentagem_coelho = (total_coelho/total)*100
porcentagem_sapo = (total_sapo/total)*100

if 1 <= int(valores[0]) <= 15:
    print('Total: {} cobaias\nTotal de coelhos: {}\nTotal de ratos: {}\nTotal de sapos: {}'.format(total, total_coelho, total_rato, total_sapo))
    print('Percentual de coelhos: {:.2f} %\nPercentual de ratos: {:.2f} %\nPercentual de sapos: {:.2f} %'.format(porcentagem_coelho, porcentagem_rato, porcentagem_sapo))
