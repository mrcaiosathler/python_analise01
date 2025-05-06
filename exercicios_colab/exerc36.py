## Exercício 36: Crie uma lista com 5 números e imprima o maior.

numeros = []

lista_num = int(input('Informe quanto números serão incluídos na sua lista: '))

for i in range(lista_num):
    numero = float(input(f'Informe o {i+1}º número da lista: '))
    numeros.append(numero)

max_num = max(numeros)

print('Este é o maior número da sua lista: ', (max_num))
