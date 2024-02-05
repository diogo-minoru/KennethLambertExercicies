"""
    Calcular o crescimento populacional de um organismo definido uma taxa de crescimento.
    O usuário deve informar o número inicial de organismos e a taxa de crescimento (maior que 0),
    o número de horas que leva para atingir essa taxa e o total de horas de crescimento.

"""

populacao_inicial = int(input("Informe a quantidade de organismos inicial: "))
taxa = int(input("Informe a taxa de crescimento da população: "))
horas = int(input("Horas para alcançar a taxa: "))
horas_inicial = horas
horas_calculo = int(input("Horas para cálculo da população: "))
populacao_final = 0

while horas_inicial <= horas_calculo:
    populacao_final = populacao_inicial * taxa
    horas_inicial += horas
    populacao_inicial = populacao_final

print(populacao_final)