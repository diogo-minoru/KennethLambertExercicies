"""
    Programa para calcular o retorno de um investimento
    
    1. O programa deve receber o valor investido, o número de anos e a taxa ao ano em %
    2. Como resultado mostrar uma tabela com as colunas (Ano, Balanço inicial, Retorno, Balanço final)
    3. Mostrar os valores ano por ano em uma tabela
    4. Mostrar os totais

"""

import pandas as pd

valor_inicial = float(input("Digite o valor total investido: "))
anos = int(input("Digite o total de ano que será investido: "))
taxa = float(input("Digite a taxa anual em que será calculado: "))/100
data = list()

for i in range(1, anos + 1):
    tabela = {"Ano": i, "Balanço Inicial": valor_inicial, "Retorno": valor_inicial * taxa, "Balanço Final": valor_inicial + valor_inicial * taxa}
    valor_inicial = valor_inicial + valor_inicial * taxa
    data.append(tabela)

dataframe = pd.DataFrame(data).set_index("Ano")
dataframe[["Balanço Inicial", "Retorno", "Balanço Final"]] = dataframe[["Balanço Inicial", "Retorno", "Balanço Final"]].applymap(lambda x: '{:,.2f}'.format(x))
dataframe[["Balanço Inicial", "Retorno", "Balanço Final"]] = dataframe[["Balanço Inicial", "Retorno", "Balanço Final"]].applymap(lambda x: float(x.replace(",", "")))

total_retorno = dataframe["Retorno"].sum()
linha_total = pd.Series({"Retorno": total_retorno}, name = "Total")

dataframe = pd.concat([dataframe, linha_total.to_frame().T])

print(dataframe)