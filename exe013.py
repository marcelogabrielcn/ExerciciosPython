sal = float(input('Digite o salário atual do funcionário: R$'))
acre = (sal/100)*15
nsal = sal + acre
print('O novo salário com 15% de acréssimo é R${:.2f}'.format(nsal))
