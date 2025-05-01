## Exercício 14: Crie um menu onde o usuário pode escolher entre exibir a data, hora ou sair.

from datetime import datetime, time, date

def calendario(op):
  return{
      'Dia': datetime.now().date(),
      'Hora': datetime.now().time(),
      'Sair': 'Okay, até mais!'
  }.get(op, 'Operação inválida')

op = input('1 - Dia\n2 - Hora\n3 - Sair\n\nEscolha o que exibir: ')
print (calendario(op))