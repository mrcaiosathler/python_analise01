import pandas

#serie = pandas.Series([10,20,30]) #estrtura unidimensional: vetor

# dados = {
#     'nome': ['Ana', 'Bia', 'Carlos'],
#     'idade': [30,10,18]
# }

# df=pandas.DataFrame(dados) #estrutura bidimensional: matriz

# print(df)

ler_base = pandas.read_csv('df_analise.csv', sep=';')

# print(ler_base.describe())

# print(ler_base.loc[1])

# print(ler_base.loc[1, 'nome'])

print(ler_base.iloc[1, 1])