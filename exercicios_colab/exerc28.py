## Exercício 28: Crie um programa que solicite 5 números ao usuário e exiba a soma deles.

soma = 0

for i in range(5):
    numero = float(input(f"Digite o {i + 1}º número: "))
    soma += numero  # Soma os números inseridos

print(f"A soma dos números é: {soma}")