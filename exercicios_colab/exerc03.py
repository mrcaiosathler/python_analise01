## Exercício 3: Verifique se um número é par ou ímpar.

#1. Pergunte ao usuário um número
#2. Anote o número informado
#3. Efetue a divisão deste número por 2 (dois).
#4. Anote o resultado desta divisão e também o resto.
#5. Verificar se o resultado da divisão é um número inteiro.
#6. Verificar se o resto da divisão é igual a zero.
#7. Em caso de ambas verificações serem verdadeiras, informar que o número é par.
#8. Em caso de uma das verificaçõs ser falsa, informar que o número é ímpar.
#9. Em caso de ambas verificações serem falsas, informar que o número é ímpar.

num = float(input('Digite um número: '))
if num % 2 == 0:
  print('Esse número é par')
else:
  print('Esse número é ímpar')

  
