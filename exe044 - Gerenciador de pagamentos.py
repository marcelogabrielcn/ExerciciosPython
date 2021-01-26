print('{:=^40}\n'.format('LOJAS MGabriel'))
#  preço do produto
preco = float(input('Digite o valor a ser pago pelo produto: R$'))
#  forma de pagamento
forma = int(input('''Qual será a forma de pagamento?
[1] - À vista no dinheiro
[2] - À vista no cartão
[3] - Parcelado no cartão\n'''))
if forma == 1:
    desc = (preco / 100) * 10  # desconto de 10%
    print(
        '\nPagando à vista no dinheiro você ganha um desconto de 10%. \nSua compra ficará no valor de R${:.2f}'.format(
            preco - desc))
elif forma == 2:
    desc = (preco / 100) * 5
    print('\nPagando à vista no cartão você ganha um desconto de 5%. \nSua compra ficará no valor de R${:.2f}'.format(
        preco - desc))
elif forma == 3:
    parc = int(input('\nEm quantas vezes deseja parcelar? '))
    if parc >= 3:
        juros = (preco / 100) * 20  # juros de 20% para compras parceladas em 3 ou mais vezes
        valpar = (preco + juros) / parc  # Valor das parcelas
        print('''Parcelando em três vezes ou mais, terá um juros de 20%.
Sua compra ficará no valor de R${:.2f}
Irá pagar {} parcelas de R${:.2f}'''.format((preco + juros), parc, valpar))
    else:
        valpar = preco / parc  # Valor das parcelas
        print('''Parcelando em até 2x você não tem juros.
Sua compra ficará no valor de R${:.2f}
Irá pagar {} parcelas de {:.2f}'''.format(preco, parc, valpar))
print('\nBoas compras!!!')
