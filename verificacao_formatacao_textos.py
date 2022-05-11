# Este Programa é para podermos formatar e verificar algo
print('********* Bem Vindo **********')
print('***Projeto Iniciando Python***')

nome = str(input("Qual Seu Nome Completo ? ").strip())
nome = nome.lower()

print("Seu nome è {}".format(nome))

if 'meurer' in nome :
    print("Nos Somos Parente")

else:
    print("não somos parentes ")