linha = '-=-' * 8
title = '\033[0;36;40mANALISANDO EMPRESTIMO\033[m'
print(linha)
print(title.center(30))
print(linha)
casa = float(input('Qual o valor do imóvel que deseja financiar? R$'))
sal = float(input('Qual valor da sua renda mensal? R$'))
tempo = int(input('Em quantos meses deseja parcelar o financiamento? R$'))

#Calculando o valor do parcelamento
parcela = casa / tempo
#A prestação não pode ser maior que 30% do salário
if parcela > (sal/100) * 30:
    print('Desculpe, sua renda mensal é insuficiente para parcelar este imóvel.')
else:
    print('Você irá pagar {} parcelas de R${:.2f}.'.format(tempo, parcela))
