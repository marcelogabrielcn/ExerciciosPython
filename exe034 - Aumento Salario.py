sal = float(input('Digite o salário:  '))
if sal > 1250:
    acre = (sal/100) * 10
    sal = sal + acre
else:
    acre = (sal/100) * 15
    sal = sal + acre
print('Você teve um aumento de R${:.2f}. Seu novo salário é de R${:.2f}'.format(acre, sal))
