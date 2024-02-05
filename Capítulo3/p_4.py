"""
    Calcular a distância total percorrida pela bola que foi solta de uma determinada altura informada pelo usuário.
    Utilizando uma taxa de 0.6 para cada quique da bola no chão. Retornar a distância total.
    Exemplo:
        Altura inicial = 10m
        Taxa = 0.6

        10m + 6m + 6m + 3.6m + 3.6m + 2,16m + 2,16m ...

"""

altura_inicial = float(input("Informe a altura inicial: "))
TAXA = 0.6
LIMITE_DISTANCIA = 0.00001
altura_final = altura_inicial * 0.6
total_percorrido = altura_inicial

while altura_final >= LIMITE_DISTANCIA:
    total_percorrido += altura_final * 2
    altura_final *= 0.6
print(total_percorrido)