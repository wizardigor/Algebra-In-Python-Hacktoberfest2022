# questão 7

# recebendo inputs
eleitores = int(input("Digite o total de eleitores: "))
maria = 0
jose = 0
joao = 0
votantes = 0

while votantes < eleitores:
    print("""
    1 - Maria
    2 - José
    3 - João
    """)
    voto=input("Digite o numero do candidato que deseja votar: ")
    if voto == "1":
        maria = maria + 1
        print("\nVocê votou na Maria")
    elif voto == "2":
        jose = jose + 1
        print("\nVocê votou no José")
    elif voto == "3":
        joao = joao + 1
        print("\nVocê votou no João")
    else:
        print("\n Digite uma opção válida!")
    votantes = votantes + 1

print(f"""
    Resultado
    Maria: {maria} votos
    José: {jose} votos
    João: {joao} votos
    """)
