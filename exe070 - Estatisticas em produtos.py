print('-' * 25)
print('    LOJÃO DO BINHÃO    ')
print('-' * 25)
continuar = ''
total = 0
maisde1k = 0
morecheap = 0
productcheap = ''

while continuar != 'X':
    produto = str(input('Digite o nome do produto: ')).strip().capitalize()
    preco = float(input('Digite o preço do produto: R$'))
    while preco <= 0:
        preco = float(input('Digite o preço do produto: R$'))
    total += preco
    if preco >= 1000:
        maisde1k += 1
    if morecheap == 0:
        morecheap = preco
        productcheap = produto
    else:
        if preco < morecheap:
            morecheap = preco
            productcheap = produto
    continuar = str(input('Pressione ENTER para continuar, X para finalizar a compra.\n')).strip().upper()

print(f'\nCompra finalizada. TOTAL R${total:.2f}')
print(f'Existe {maisde1k} produto(s) que custa mais de R$1.000,00')
print(f'O produto mais barato foi a(o) {productcheap}, que custa R${morecheap:.2f}')
