num = int(input('Digite um número inteiro: '))
print("""Podemos fazer as seguintes convesões:
1 - Para binário
2 - Para octal
3 - Para hexadecimal""")
base = int(input('Digite 1, 2 ou 3 para sua conversão: '))
if base == 1:
    print('O número {}, convertido pra Binário é {}'.format(num, bin(num)[2:]))
elif base == 2:
    print('O número {}, convertido pra Octal é {}'.format(num, oct(num)[2:]))
elif base == 3:
    print('O número {}, convertido pra Hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('Número inválido!')
