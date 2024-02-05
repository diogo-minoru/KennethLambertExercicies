"""
    Exercício 3

    Programa deve calcular o total do valor de locação de vídeo de uma locadora para um cliente
    O cliente deve informar o tipo e a quantidade para cada um
    Os tipos e os valores são:
        Vídeos novos = $3,00 por noite
        Vídeos antigos = $2,00 por noite

"""

VALOR_NOVO = 3
VALOR_ANTIGO = 2

qtde_novos = int(input("Informe a quantidade de vídeos novos a serem locados: "))
tempo_novos = int(input("Informe a quantidade de noites que será locado os vídeos novos: "))

qtde_antigos = int(input("Informe a quantidade de vídeos antigos a serem locados: "))
tempo_antigos = int(input("Informe a quantidade de noites que será locado os vídeos antigos: "))

valor_novos = qtde_novos * tempo_novos * VALOR_NOVO
valor_antigos = qtde_antigos * tempo_antigos * VALOR_ANTIGO

valor_total = valor_novos + valor_antigos

print(f"O valor total de locação é de ${valor_total}")