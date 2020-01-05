k = 1
y = 7    
cont = 0
for i in range(0, 5):
    for j in range(0, 3):

        cont += 1

        print('I={} J={}'.format(k, y))
        
        y = y - 1

        if cont == 3:
            y = 9
        elif cont == 6:
            y = 11
        elif cont == 9:
            y = 13
        elif cont == 12:
            y = 15
        
    k = k + 2
    




  
