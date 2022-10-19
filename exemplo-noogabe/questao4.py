# questão 4

# definindo a função
def parImpar(number):
    if number % 2 == 0:
        return "par"
    else:
        return "impar" 

# recebendo inputs
number = int(input("Digite um numero: "))

# chamando a função
print("\nO numero digitado é", (parImpar(number)))