print('Vamos veríficar se as frases são palíndromos.')

'''Palindromos são frases ou falavras que podem ser lidas de frente pra trás
 ou de trás pra frente e ela continuará com o mesmo sentido.
 exemplos: 
 A SACADA DA CASA
 APOS A SOPA
 A TORRE DA DERROTA
 O LOBO AMA O BOLO
 ANOTARAM A DATA DA MARATONA
 '''
print('Ou seja, são iguais lida de trás pra frente ou de frente pra trás.')
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
 # Invés de usar o for, podemos usar a seguinte linha: inverso = junto[::-1]. é um macete de fatiamento.
print('O inverso de {}, é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palindromo!!!')
else:
    print('A frase não é um palindromo.')
