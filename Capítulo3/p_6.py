"""
    Utilizar a formula pi = 4 * (1 - 1/3 + 1/5 - 1/7 + ...) para encontrar o valor aproximado de pi
    com base no número de iterações informadas pelo usuário

"""

print(4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + 1/13 - 1/15 + 1/17 - 1/19 + 1/21 - 1/23 + 1/25))

iteracoes = int(input("Número de iterações: "))
aproximacao = 0

for i in range(0, iteracoes + 1):
    aproximacao = aproximacao + valor
    for x in range(1, iteracoes ** 2):
        valor = 