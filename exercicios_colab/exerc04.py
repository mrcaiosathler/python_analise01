## Exercício 4: Verifique se um ano é bissexto.

#1. Pergunte ao usuário um ano.
#2. Anote o ano informado pelo usuário.
#3. Verificar se o número informado é múltiplo de 4, mas não é múltiplo de 100.
#4. Verificar se o número informado é múltiplo de 400.
#5. Se as verificações #3 ou #4 forem verdadeiras, informar que o ano é bissexto.
#6. Se as verificações #3 e #4 forem falsas, informar que o ano não é bissexto.

ano = int(input('Informe um ano, com quatro dígitos: '))
if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
  print('O ano',ano,'é bissexto')
else:
  print('O ano',ano,'não é bissexto')

  