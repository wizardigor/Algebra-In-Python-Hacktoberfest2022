# questão 5

# definindo a função parImpar
def parImpar(number):
    if number % 2 == 0:
        return "par"
    else:
        return "impar" 

# definindo a função positivoNegativo
def positivoNegativo(number):
    if number > 0:
        return "positivo"
    elif number == 0:
        return "zero"
    else:
        return "negativo" 

# definindo a função inteiroDecimal
def inteiroDecimal(number):
    if round(number) == number:
        return "inteiro"
    else:
        return "decimal"

# recebendo inputs
number = float(input("Digite um numero: "))

ans=True
while ans:
    print("""
    1 - Verificar se é impar ou par
    2 - Verificar se é positivo ou negativo
    3 - Verificar se é inteiro ou decimal
    4 - Sair
    """)
    ans=input("O que você gostaria de fazer? ")
    if ans=="1":
      print("\nO numero digitado é", (parImpar(number)))
    elif ans=="2":
      print("\nO numero digitado é", (positivoNegativo(number)))
    elif ans=="3":
      print("\nO numero digitado é", (inteiroDecimal(number)))
    elif ans=="4":
      print("\nByebye") 
      ans = None
    else:
       print("\n Digite uma opção válida!")