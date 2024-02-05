dicionario = dict()

dicionario["Nome"] = "Diogo Minoru Kokubu"
dicionario["Idade"] = 26


"""
print(dicionario.get("Nome", None))
print(dicionario.items())
"""

"""
for key, value in dicionario.items():
    print(key, value)
"""
dicionario["Idade"] = -dicionario["Idade"]
print(len(dicionario))
print(list(dicionario.keys()))
print(list(dicionario.values()))
