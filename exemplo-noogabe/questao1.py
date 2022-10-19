# questão 1

# definindo a função
def areaQuadrado(lateral):
    area = lateral ** 2
    return area * 2

# recebendo inputs
lateral = int(input("Digite o valor da lateral do quadrado: "))

# chamando a função
print("O valor do dobro da área do quadrado é de: ", (areaQuadrado(lateral)))

