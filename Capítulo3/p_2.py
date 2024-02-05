"""
    Receber o valor de três arestas de um triangulo e dizer se forma um angulo de 90°
"""

aresta1 = float(input("Valor da aresta 1: "))
aresta2 = float(input("Valor da aresta 2: "))
aresta3 = float(input("Valor da aresta 3: "))

arestas = [aresta1, aresta2, aresta3]
arestas.sort()


if arestas[2] ** 2 == arestas[0] ** 2 + arestas[1] ** 2:
    print("O triangulo faz um angulo de 90°.")
else:
    print("O triangulo não faz angulo de 90°.")
