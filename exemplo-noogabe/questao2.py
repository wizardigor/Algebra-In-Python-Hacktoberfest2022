# questão 2

# definindo a função
def celciusToFahrenheit(f):
    c = 5 * ((f-32) / 9)
    return c

# recebendo inputs
f = float(input("Digite a temperatura em fahrenheit: "))

# chamando a função
print("A temperatura em celcius é: ", (celciusToFahrenheit(f)))

