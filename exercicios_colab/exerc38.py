## Exercício 38: Crie uma lista com 5 nomes e remova o último nome.


chamada = []

cont_list = int(input('Informe quantos nomes serão incluídos na sua lista: '))

for i in range(cont_list):
    nomes = input(f'Informe o {i+1}º nome da sua lista: ')
    chamada.append(nomes)

chamada.pop()

print('Essa é sua lista após remover o último nome informado: ', chamada)