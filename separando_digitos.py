print('********* Bem Vindo **********')
print('***Projeto Iniciando Python***')

numero = int(input("Digite um Numero de 0 a 9999"))
num = str(numero)

print("Vamos analisar o numero digitado {} ".format(numero))
print("O numero é composto por {} Unidade ".format(num[3]))
print("{} Desena ". format(num[2]))
print("{} Centena ".format(num[1]))
print("{} Milhar ".format(num[0]))

#Tem outra maneira

#d = numero // 10 % 10
#c = numero // 100 % 10
#m = numero // 1000 % 10

#print("Vamos analisar o numero digitado {} ".format(numero))
#print("O numero é composto por {} Unidade ".format(u))
#print("{} Desena ". format(d))
#print("{} Centena ".format(c))
#print("{} Milhar ".format(m))