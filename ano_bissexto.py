print('********* Bem Vindo **********')
print('***Projeto Iniciando Python***')

ano = int(input("Digite o ano "))

ano_bixesto = ano % 4

if ano_bixesto == 0:
    print('O ano {} é Bissexto'.format(ano))
else:
    print("O ano {} NÂO é Bissexto ".format(ano))