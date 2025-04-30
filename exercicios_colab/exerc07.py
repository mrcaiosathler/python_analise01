## Exercício 7: Verifique se já posso ir embora da aula de Análise de Dados sem assinar a folha.

"""hora = float(input('Informe as horas que pretende sair, seguindo o formato "hora.minuto": '))
if hora >= 21.45:
  print('Você já pode ir embora sem assinar a lista! Bom descanso.')
else:
  print('Você ainda não pode ir embora, espere um pouco mais!')  """

from datetime import datetime, time
print(datetime.now().time())
if datetime.now().time() >= time(hour=00, minute=45):
  print('Pode sair!')
else:
  print('Não pode!')


