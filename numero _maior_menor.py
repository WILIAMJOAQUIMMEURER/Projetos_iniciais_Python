print('********* Bem Vindo **********')
print('***Projeto Iniciando Python***')

n1 = int(input("Digite um numero"))
n2 = int(input("Digite outro numero"))
n3 = int(input("Digite outro numero"))

if n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n1 and n2 > n3:
    maior = n2
else:
    maior = n3

if n1< n2 and n1 < n3:
    menor = n1
elif n2 < n1 and n2 < n3:
    menor = n2
else:
    menor = n3

print('O numero maior foi {} e o nemor foi {}'.format(maior,menor))