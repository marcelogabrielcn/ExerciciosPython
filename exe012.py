preco = float(input('Digite o preço do produto: R$'))
desc = (preco/100)*5
npreco = preco - desc
print('O produto com desconto de 5% de desconto custa R${:.2f}'.format(npreco))
