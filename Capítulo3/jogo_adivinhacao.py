import random

minimo = int(input("Digite o valor minimo: "))
maximo = int(input("Digite o valor máximo: "))
numero_correto = random.randint(minimo, maximo)

tentativa = int(input("Tente adivinhar o valor: "))
contagem = 0
while True:
    contagem += 1
    if tentativa < numero_correto:
        print("Tente um número maior: ")
    elif tentativa > numero_correto:
        print("Tente um número menor: ")
    else:
        print("Parabéns, você acertou o número!!!")
        print(f"Número sorteado: {numero_correto} \n Chute: {tentativa} \n Tentativas: {contagem}")
        break
    tentativa = int(input("Tente adivinhar o valor: "))