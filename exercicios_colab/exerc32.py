## Exercício 32: Some todos os números de uma lista.

numeros = []

lista_num = int(input('Informe quantos números terá em sua lista: '))

for i in range (lista_num):
    numero = float(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)

soma = sum(numeros)

print(f"A soma dos números é: {soma} ")