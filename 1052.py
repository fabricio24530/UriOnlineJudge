def meses(a):
    dicionario_meses = { 
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'July',
        8: 'August',
        9: 'September',
        10: 'October',
        11: 'November',
        12: 'December'
    }

    return print(dicionario_meses[a])

num = int(input())

if num >= 1 and num <=12:
    meses(num)
