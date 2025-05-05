## Exercício 33: Multiplique cada número de uma lista por 2 e imprima o resultado.

numeros = []

lista_num = int(input('Informe quantos números terá em sua lista: '))

for i in range (lista_num):
    numero = float(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)

dobro_num = [numero*2 for numero in numeros]

print(f"O dobro de cada número da sua lista é: {dobro_num} ")