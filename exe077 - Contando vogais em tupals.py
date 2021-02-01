palavras = ('python', 'rubi', 'java', 'bootstrap',
            'django', 'Microsoft', 'Apple', 'Linux',
            'banco', 'redes', 'computadores', 'sies')
print('Vamos ver as vogais que temos nas palavras. ')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letras in p:
        if letras in 'aeiou':
            print(letras, end=' ')
print('\nFim')
