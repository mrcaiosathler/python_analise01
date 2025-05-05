## Exercício 31: Percorra uma lista de frutas e imprima cada uma.

frutas = []

for i in range (5):
    fruta = input(f'Digite o nome da {i+1}ª fruta da sua lista: ')
    frutas.append(fruta)

print('\nLista de Compras:')
for fruta in frutas:
    print (fruta)
