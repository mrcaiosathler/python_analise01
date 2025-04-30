## Exercício 2: Peça dois números e exiba o maior.

#1. Pergunte ao usuário um número.
#2. Anote esse número.
#3. Pergunte ao usuário um outro número, diferente do primeiro.
#4. Anote também esse número.
#5. Verificar se o primeiro número é maior que o segundo número.
#6. Anotar o maior número dentre os dois.
#7. Exibir o número anotado após a verificação do passo #5.

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite agora o segundo número: '))
if num1 > num2:
  print('O número maior é: ', num1)
elif num1 == num2:
  print('Os números são iguais')
else:
  print('O número maior é: ', num2)

  