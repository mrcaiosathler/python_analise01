## Exercício 15: Implemente um programa que identifica o dia da semana baseado em um número (1 = Segunda, 7 = Domingo).

def numeros(op):
  return{
      '1': 'Segunda',
      '2': 'Terça',
      '3': 'Quarta',
      '4': 'Quinta',
      '5': 'Sexta',
      '6': 'Sábado',
      '7': 'Domingo',
  }.get(op, 'Operação inválida')

op = input('Escolha um número: 1, 2, 3, 4, 5, 6 ou 7: ')
print ('Resultado: ', numeros(op))