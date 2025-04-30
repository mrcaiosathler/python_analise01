## Exercício 1: Verifique se um número é positivo, negativo ou zero.


#1. Pergunte o número ao usuário.
#2. Anote o número informado pelo usuário.
#3. Verifique se o número informado é maior, menor ou igual ao número zero.
#4. Se uma das verificações anteriores for verdadeira, considerar as demais falsas
#5. Pegue o resultado verdadeiro da verificação anterior.
#6. Se o número for maior que zero, informar que é um número positivo.
#7. Se o número for igual a zero, informar que é zero.
#8. Se o número for menor que zero, informar que é um número negativo.

num = float(input('Digite um número: '))
if num > 0:
  print('O número é positivo')
elif num < 0:
  print('O número é negativo')
else:
  print('O número é zero')
