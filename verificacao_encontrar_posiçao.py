# Este Programa é para podermos formatar e verificar algo
print('********* Bem Vindo **********')
print('***Projeto Iniciando Python***')

frase = str(input("Digite uma Frase").strip())
frase = frase.lower()

print("na frase {} temos:".format(frase))

print("A letra a aparece {} veses".format(frase.count('a')))
print("A primeira letra a aparece na posiçao {}".format(frase.find("a")))
print('A ultima vez que o a aparece é na posiçao {}'.format(frase.rfind('a')))