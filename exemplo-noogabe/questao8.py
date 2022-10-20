# questão 8

# recebendo inputs
tabuada = int(input("Qual tabuada você quer visualizar? "))

for num in range(0, 11):
    print(f"""{num} x {tabuada} = {num*tabuada}""")
