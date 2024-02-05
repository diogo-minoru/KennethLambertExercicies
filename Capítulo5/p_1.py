"""
    Criar uma função para calcular a média e a moda de uma lista de números
"""

def main():
    lista = list()
    while True:
        numero = input("Digite um número para adicionar à lista: ")
        if numero != "":
            lista.append(int(numero))
        else: break
    resultado_media = media(lista)
    resultado_moda = moda(lista)
    return print(f"A média dos valores inseridos é: {resultado_media:.2f} A moda é {resultado_moda}")

def media(valores_media):
    return sum(valores_media) / len(valores_media)


def moda(valores_moda):
    # Contar a frequência de cada elemento
    contagem = {}
    for elemento in valores_moda:
        contagem[elemento] = contagem.get(elemento, 0) + 1

    # Encontrar o(s) elemento(s) com a maior contagem
    moda_elementos = [k for k, v in contagem.items() if v == max(contagem.values())]

    # Se todos os elementos têm a mesma frequência, a lista não tem moda
    if len(moda_elementos) == len(set(valores_moda)):
        return None
    else:
        return moda_elementos


if __name__ == "__main__":
    main()