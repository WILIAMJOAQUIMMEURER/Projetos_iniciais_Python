print('********* Bem Vindo **********')
print('***Projeto Iniciando Python***')


nome = str(input('Escreva seu nome Completo')).strip()
separa = nome.split()

pula_linha
print('Seu nome em letras maiusculas fica {}'.format(nome.upper()))
pula_linha
print('Seu nome em letras minusculas fica {}'.format(nome.lower()))
pula_linha
print('A quantidadde de caracteres é {}'.format(len(nome)- nome.count(' ')))
pula_linha
print('seu primeiro nome é {} e tem {} caracteres'.format(separa[0], len(separa[0])))
