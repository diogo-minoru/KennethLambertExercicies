"""
    Exercício 4:

    Programa para receber o valor do raio de uma esfera (float) e retornar os valores de:
        Diametro
        Circunferência
        Área da Superfície
        Volume   
    
"""

import math

raio = float(input("Informe o valor do raio da esfera: "))

diametro = raio * 2

circunferencia = math.pi * raio ** 2

area = 4 * math.pi * raio **2

volume = (4/3) * math.pi * raio ** 3

print(f"Raio = {raio} \n Diâmetro = {diametro} \n Circunferência = {circunferencia} \n Área = {area} \n Volume = {volume}")