first = int(input('Qual o primeiro termo da PA? '))
razao = int(input('Digite a razão da PA: '))
decimo = first + (10 - 1) * razao
for c in range(first, decimo + razao, razao):
    print(c)
print('the end')
