matriz = [[], [], [], [], [], [], [], [], []]
cont = 0
valpar = 0  # Valores pares
tcol = 0  # Valores da terceira coluna
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[cont].append(int(input(f'Digite um valor para posição {linha}, {coluna}: ')))
        cont += 1
for i, v in enumerate(matriz):
    for n in v:
        if n % 2 == 0:
            valpar += n
        if (i+1) % 3 == 0:
            tcol += n
print('-=-' * 20)
print(f' {matriz[0]} {matriz[1]} {matriz[2]} '
      f'\n {matriz[3]} {matriz[4]} {matriz[5]} '
      f'\n {matriz[6]} {matriz[7]} {matriz[8]} ')
print('-=-' * 20)
print(f'A soma dos valores pares foi: {valpar}')
print(f'A soma dos valores da terceira coluna foi: {tcol}')
