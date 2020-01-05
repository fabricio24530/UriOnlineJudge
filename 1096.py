k = 1
y = 7
for i in range(0, 5):
    for j in range(0, 3):
        print('I={} J={}'.format(k, y))
        y = y - 1
        if y < 5:
            y = 7
    k = k + 2
