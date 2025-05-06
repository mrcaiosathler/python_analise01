## Exercício 37: Crie uma lista e inverta a ordem dos elementos.

lista = []

cont_list = int(input('Informe quantos elementos serão incluídos na sua lista: '))

for i in range(cont_list):
    elementos = input(f'Informe o {i+1}º elemento da sua lista: ')
    lista.append(elementos)

invert_list = lista [::-1]

print('Essa é a ordem invertida da inclusão dos termos na sua lista: ', invert_list)