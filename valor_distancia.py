print('********* Bem Vindo **********')
print('***Projeto Iniciando Python***')

distancia = int(input('Qual a distacia da viagem ?'))
d1 = distancia * .5
d2 = distancia * .45

if distancia < 200:
    print('A distancia é de {} e custa 0,50 por km, e vai custar {}'.format(distancia, d1))
else:
    print('A distancia é de {} e custa 0,45 por km, e vai custar {}'.format(distancia, d2))