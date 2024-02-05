"""
    Programa para receber três valores de arestas de um triangulo e dizer se é um triangulo é equilatero ou não.

"""

aresta1 = float(input("Valor da aresta 1: "))
aresta2 = float(input("Valor da aresta 2: "))
aresta3 = float(input("Valor da aresta 3: "))

if aresta1 == aresta2 == aresta3:
    print("Triangulo equilatero.")
else:
    print("Triangulo não equilatero.")