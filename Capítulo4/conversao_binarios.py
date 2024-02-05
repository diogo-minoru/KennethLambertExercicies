# binario para decimal
"""
binario = 11001
decimal = 0
expoente = len(str(binario)) - 1
for n in str(binario):
    decimal += int(n) * (2 ** expoente)
    expoente -= 1
print(decimal)
"""

# Decimal para binário
"""
decimal = 64
binario = list()

while decimal != 0:
    resto = decimal % 2
    binario.append(resto)
    decimal = decimal // 2
    print(decimal)
print(binario[::-1])
"""

# Octa para decimal
"""
octa = 127
decimal = 0
expoente = len(str(octa)) - 1
for n in str(octa):
    decimal += int(n) * (8 ** expoente)
    expoente -= 1
print(decimal)
"""

# Hexa para decimal
"""
hexa_para_decimal = dict(zip(["A", "B", "C", "D", "E", "F"], [10, 11, 12, 13, 14, 15]))
hexa = 47

print(hexa_para_decimal)
"""

