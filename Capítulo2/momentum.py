"""
    Exercício 5

    Programa para calcular o momento de um objeto.
    O momento de um objeto é a multiplicação de sua massa pela sua velocidade
    O programa deve receber a massa do objeto (kilos) e a valocidade (m/s) e retornar o momento.

    Exercício 6

    Utilizar o código do exercício 5 e calcular a energia cinética do objeto dado pela fórmula

        Ke = (1/2)mv²
        m = massa
        v = velocidade
"""

massa = float(input("Digite a massa do objeto em kilos: "))
velocidade = float(input("Digite a velocidade do objeto em m/s: "))

momento = massa * velocidade
energia_cinetica = (1/2) * massa * velocidade ** 2

print(f"O valor do momento é {momento} kgm/s e o valor da energia cinetica é {energia_cinetica} kgm²/s²")
