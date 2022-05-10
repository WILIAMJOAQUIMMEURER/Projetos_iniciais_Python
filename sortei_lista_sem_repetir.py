import random
print('********* Bem Vindo **********')
print('***Projeto Iniciando Python***')

p1 = input("nome")
p2 = input("nome")
p3 = input("nome")
p4 = input("nome")
p5 = input("nome")
p6 = input("nome")

pessoas_lista = [p1,p2,p3,p4,p5,p6]

random.shuffle(pessoas_lista)

for l in pessoas_lista:
    print(l)