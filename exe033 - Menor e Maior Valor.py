n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite outro número: '))
#Verifiando o menor número
if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
#Verificando o maior número
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n3
if n3 > n1 and n3 > n2:
    maior = n3
print('O maior número é {}, e o menor é {}'.format(maior, menor))
