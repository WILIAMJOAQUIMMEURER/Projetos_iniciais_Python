print('********* Bem Vindo **********')
print('***Projeto Iniciando Python***')

preço = float (input('Qual o preço  do produto ?'))
descoto = float(input("Qual a porcentagem de Desconto ?"))

valor_desconto = float((preço * descoto) /100)

valor_novo = preço - valor_desconto

print('O valor do desconto foi {} o preço com desconto {}'.format(valor_desconto,valor_novo))