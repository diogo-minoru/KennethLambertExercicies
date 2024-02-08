""""
    Escrever um programa para calcular a raíz quadrada de um número
    admitindo uma tolerância de 0.000001 em relação ao valor obtido utilizando a função sqrt
"""

import math

TOLERANCIA = 0.000001

def main():
    x = float(input("Digite um valor pára encontrar a raiz quadrada: "))
    return print(f"Valor aproximado da raiz: {raiz_aproximada(x)} \nRaiz utilizando a função: {math.sqrt(x)}")

def raiz_aproximada(n):
    estimado = 1
    while True:
        estimado = (estimado + n / estimado) / 2
        diferenca = abs(n - estimado ** 2)
        if diferenca <= TOLERANCIA:
            break
    return estimado

if __name__ == "__main__":
    main()