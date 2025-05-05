## Exercício 30: Crie um programa que peça 5 números e exiba apenas os números pares.

numeros = [float(input(f'Digite o {i+1}º número:')) for i in range(5)]
pares = [num for num in numeros if num % 2 == 0] 

print(f"Os números pares são: {pares}")

