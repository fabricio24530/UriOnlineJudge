
number = int(input())

if 2 < number < 1000:
    for i in range(1, 11):
        print('{} x {} = {}'.format(i, number, i*number))

