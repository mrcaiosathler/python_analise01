## Exercício 13: Crie um programa que traduza números de 1 a 5 para palavras (1 = um, 2 = dois...).

def numeros(op):
  return{
      '1': 'Um',
      '2': 'Dois',
      '3': 'Três',
      '4': 'Quatro',
      '5': 'Cinco',
  }.get(op, 'Operação inválida')

op = input('Escolha um número para ser escrito por extenso: 1, 2, 3,4 ou 5: ')
print ('Resultado: ', numeros(op))