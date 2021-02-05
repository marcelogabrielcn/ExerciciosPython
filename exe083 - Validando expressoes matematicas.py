frase = str(input('Digite a expressão: '))
lista = []
for caractere in frase:
    if caractere == '(':
        lista.append('(')
    elif caractere == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Esta expressão é váldida!')
else:
    print('Essa expressão é inválida')
