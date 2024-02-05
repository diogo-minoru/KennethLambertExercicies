"""
    Encontrar o maior divisor comum entre dois números positivos inteiros
    1. Calcular o resto da divisão entre o maior número e o menor número
    2. Substituir o maior número pelo menor número e o menor número pelo restante da divisão
    3. Repetir o processo até que o menor número é zero
"""

divisor_1 = int(input("Informe um número: "))
divisor_2 = int(input("Informe outro número: "))

maior = max(divisor_1, divisor_2)
menor = min(divisor_1, divisor_2)
resto = 0
iteracao = 0

while menor != 0:
    resto = maior % menor
    maior = menor
    menor = resto
    iteracao += 1
    print(f"Iteracao: {iteracao} | Maior: {maior} | Menor: {menor} | Resto: {resto}")

print(f"O maior divisor comum entre os números {divisor_1} e {divisor_2} é: {maior}")
