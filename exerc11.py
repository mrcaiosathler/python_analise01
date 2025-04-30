## Exercício 11: Crie um menu onde o usuário pode escolher entre somar, subtrair, multiplicar e dividir dois números.

def operacao(op, a, b):
  return{
      '1': a+b,
      '2': a-b,
      '3': a*b,
      '4': a/b if b != 0 else 'Divisão por zero não é aceita'
  }.get(op, 'Operação inválida')

op = input('Escolha: 1 - Soma, 2 - Sub, 3 - Mult, 4 - Div: ')
a, b = map(int, input ('Digite dois números: ').split())
print ('Resultado: ', operacao(op, a, b))