print('********* Bem Vindo *********' )
print('***Projeto Iniciando Python***')

dinheiro = float(input("Qual valor em Reais ?"))

cotaçao_dolar = float(input("Qual cotaçao atual do Dolar ?"))

conversao = dinheiro / cotaçao_dolar

print("O seu valor de  {} R$ poderia comprar {} Dolares ".format(dinheiro,conversao))