## Exercício 34: Conte quantas palavras existem em uma lista de palavras.

palavras = []

lista_palavras = int(input('Informe quantas palavras terá em sua lista: '))

for i in range (lista_palavras):
    palavra = input(f"Digite a {i + 1}ª palavra: ")
    palavras.append(palavra)

cont_palavras = len(palavras)

print(f"Parece que sua lista tem {cont_palavras} palavras! ")