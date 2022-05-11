import random
print('********* Bem Vindo **********')
print('***Projeto Iniciando Python***')

print()
print("Estou Pensando em um numero de 0 a 10 tente adivinha !")

numero_secreto = round(random.randrange (1,10) )
tentativa = 1
while (tentativa<=3):

    chute= int(input("Digite um numero de 0 a 10 "))

    if chute == numero_secreto:
        print("parabens Voce acertou")
        break
    else:
        print("Voce errou, tentativa {} de 3".format(tentativa))
        tentativa = tentativa+1

print("Fim de Jogo")



