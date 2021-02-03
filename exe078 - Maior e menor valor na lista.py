num = []
for c in range(0, 5):
    num.append(int(input(f'Digite um valor na posição {c+1}: ')))
print(f'\nOs valores digitados foram: {num}')
print(f'O maior valor foi {max(num)} nas posições ', end='')
for i, v in enumerate(num):
    if v == max(num):
        print(f'{i+1}...', end='')
print(f'\nO menor valor foi {min(num)} na posição ', end='')
for i, v in enumerate(num):
    if v == min(num):
        print(f'{i+1}...', end='')
print('\nFim')
