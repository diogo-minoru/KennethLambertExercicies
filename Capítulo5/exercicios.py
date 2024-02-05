"""
    Função para informar se um número é par ou ímpar
"""

# def main():
#     numero = float(input("Digite um numero: "))
#     return even(numero)

# def even(number):
#     if number % 2 == 0:
#         print(f"O número {number} é par.")
#     else:
#         print(f"O número {number} é Ímpar.")

# if __name__ == "__main__":
#     main()


"""
    Função para receber dois valores e retornar a soma de todos os números entre os dois valores
    incluindo o limite superior
"""

def main():
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    maior = max(n1, n2)
    menor = min(n1, n2)
    resultado = soma_numeros(menor, maior)
    print(f"A soma de todos os números entre os valores {menor} e {maior} é: {resultado} ")

def soma_numeros(limite_inferior, limite_superior):
    soma = 0
    for n in range(limite_inferior, limite_superior + 1):
        soma += n
    return soma

if __name__ == "__main__":
    main()