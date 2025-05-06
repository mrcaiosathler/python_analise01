## Exercício 39: Ordene uma lista de números.

list_num = []

cont_list = int(input('Informe quantos números serão incluídos na sua lista: '))

for i in range (cont_list):
    numeros = float(input(f'Informe o {i+1}º número da sua lista: '))
    list_num.append(numeros)

ord_list = sorted(list_num)
ord_desc_list = sorted(list_num, reverse=True)

print('Essa é a sua lista de números ordenada de forma crescente: ', ord_list)
print('Essa é a sua lista de números ordenada de forma decrescente: ', ord_desc_list)