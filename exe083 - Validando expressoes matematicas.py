letras = list(str(input('Digite a expressão: ')))
#print(letras)
#print(letras.count('('), letras.count(')'))
if letras.count('(') == letras.count(')'):
    print('Esta expressão é valida!')
else:
    print('Esta expressão é inválida!')
