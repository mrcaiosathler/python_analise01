## Exercício 27: Crie um programa que peça um número e imprima sua contagem regressiva até 0.

numero = int(input('Informe o número para contagem regressiva: '))

while numero >= 0:
    print(numero)
    numero -= 1
