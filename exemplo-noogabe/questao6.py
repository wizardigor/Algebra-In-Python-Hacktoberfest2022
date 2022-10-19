# questão 6

# recebendo inputs e adicionando em um array
numeros = []
for num in range(1, 6):
    numeros.append(int(input("Digite um número: ")))

# define a primeira posição do array como valor inicial de maiorNumero
maiorNumero = numeros[0]

# percorre o array
cont = 1
while cont < len(numeros):
# verifica se o numero atual é maior do que maiorNumero
# se sim, maiorNumero passa a ser o numero atual
    if numeros[cont] > maiorNumero:
        maiorNumero = numeros[cont]
    cont = cont + 1
        
print ("O maior número é " + str (maiorNumero))
