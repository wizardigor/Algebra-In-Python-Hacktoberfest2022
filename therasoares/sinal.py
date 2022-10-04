import time #biblioteca utilizada para definir tempo das mensagens
print("Analise a seguinte expressão 85-{50-[15-(12-8)]}")
print("\n")
exp1 = " " #Definir valor vazio para validar a função while
resp_esp1 = "parenteses" #Definir a resposta esperada

while exp1 != resp_esp1: #Condição While
    exp1 = str(input("Qual o primeiro sinal a ser resolvido? "))
    print("\n")
    if exp1 == resp_esp1: #Condição verdadeira da função
        print("Você acertou a primeira expressão")
        print("Com isso a subtração (12-8) é: 4")
        print("\n")
        time.sleep(1.5)
    else:
        print("Sua resposta não está correta, tente novamente")
        print("\n")
print("Nossa expressão agora é 85-{50-[15-4]}")
print("\n")