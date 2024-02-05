"""
    Criar um programa onde o usuário informe vários números e o programa encerra quando ele aperta enter
    Após, deve retornar o valor da soma e da média
"""

numeros = 0
soma = 0

while True:
    numero = input("Digite um número: ")
    if numero != "":
        soma += float(numero)
        numeros += 1
    else: break

print(f"Soma: {soma:.2f}, media: {(soma/numeros):.2f}")