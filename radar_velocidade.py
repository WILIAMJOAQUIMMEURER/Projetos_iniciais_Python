print('********* Bem Vindo **********')
print('***Projeto Iniciando Python***')


velocidade = int(input("Qual a velocidade do veiculo?"))

velocidade_maxima = 60
multa = (velocidade - velocidade_maxima) * 7
if velocidade <= velocidade_maxima:
    print("parabens Você esta dentro do limite de {}".format(velocidade_maxima))

else:
    print("Voce utrapassou o limite de {} e tera uma multa de {} R$ ".format(velocidade_maxima,multa))
    print('Na proxima não coloque a vida de ninguem em risco e fique dentro do limite')