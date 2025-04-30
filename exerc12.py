## Exercício 12: Crie um menu para converter temperaturas entre Celsius, Fahrenheit e Kelvin.

def temperaturas(op, t):
  return{
      'Fahrenheit': (t * 1.8)+32,
      'Kelvin': t + 273.15,
  }.get(op, 'Operação inválida')

t = float(input ('Digite a temperatura, em Celsius: '))
op = input('Escolha para qual temperatura converter: Fahrenheit ou Kelvin? ')
print ('Resultado: ', temperaturas(op, t))