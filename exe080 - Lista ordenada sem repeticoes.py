lista = []
for n in range(0, 5):
    num = int(input('Digite um número: '))
    while num in lista:
        print('Ops, este valor já esta na lista.')
        num = int(input('Digite um número: '))
    if n == 0 or num > max(lista):
        lista.append(num)
        print('Valor adicionado ao final da lista')
    elif num < min(lista):
        lista.insert(0, num)
        print('Valor adicionado na posição 0')
    else:
        i = 0
        while i < len(lista):
            if num < lista[i]:
                lista.insert(i, num)
                print(f'Valor adicionado na posição {i}')
                break
            i += 1
        # Essa parte eu não consegui fazer sozinho, assisti o vídeo de resolução e depois compreendi a lógica.
        # Basicamente é forçado um loop que vai do índece (i) 0 até o i = 5 que é a quantidade max de [lista]
        # Dentro do loop verifica se o n é menor que o valor na posição i, o break é para não ter infinity loop
print(lista)
