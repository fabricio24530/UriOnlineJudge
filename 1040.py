# -*- coding: utf-8 -*-

notas = input().split(' ')

media = ((float(notas[0]) * 2) + (float(notas[1]) * 3) + (float(notas[2]) * 4) + (float(notas[3]) * 1)) / 10

print('Media: {:.1f}'.format(media))

if media >= 7.0:
    print('Aluno aprovado.')
elif media < 5.0:
    print('Aluno reprovado.')
elif media >= 5 and media <= 6.9:
    print('Aluno em exame.')
    nota_exame = float(input())
    print('Nota do exame: {:.1f}'.format(nota_exame))
    nova_media = (media + nota_exame) / 2
    if nova_media >= 5:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado')
    print('Media final: {:.1f}'.format(nova_media))




