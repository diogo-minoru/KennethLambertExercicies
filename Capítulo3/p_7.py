"""
    Calcular o crescimento do salário de um professor que cresce em 2% por ano por no máximo 10 anos
    Retornar o resultado em formato de uma tabela
"""
import pandas as pd

total_anos = int(input("Digite o total de anos: "))
salario_inicial = float(input("Digite o salário inicial: "))
TAXA = 0.02
salario_final = salario_inicial

dataframe = list()

for i in range (1, total_anos + 1):
    # print('{:.2f}'.format(salario_final))
    linha = {"Ano": i, "Salario": salario_final, "Aumento": salario_final * TAXA}
    dataframe.append(linha)
    salario_final =  salario_final + (salario_final * TAXA)

data = pd.DataFrame(dataframe).set_index("Ano")
data[["Salario", "Aumento"]] = data[["Salario", "Aumento"]].applymap(lambda x: '{:,.2f}'.format(x))
data[["Salario", "Aumento"]] = data[["Salario", "Aumento"]].applymap(lambda x: float(x.replace(",", "")))


print(data)