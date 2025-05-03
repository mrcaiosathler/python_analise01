## Exercício 29: Imprima todas as vogais de uma string digitada pelo usuário.

def imprimir_vogais(texto):
    vogais = "aeiouAEIOU"

    for caractere in texto:
        if caractere in vogais:
            print(caractere)

texto = input('Digite uma frase, ou palavra e eu irei imprimir apenas as vogais: ')
imprimir_vogais(texto)