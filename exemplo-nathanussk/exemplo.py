# importando a biblioteca numpy do Python 
import numpy as np

# criando a função principal
def main():
    
    # menu de escolhas do progama em um loop com uma ordem de parada
    while True: 
    
        print("\nEscolha uma das opções de operações com matrizes abaixo:")
        print("   1 - Soma entre duas matrizes.")
        print("   2 - Subtração entre duas matrizes.")
        print("   3 - Multiplicação entre duas matrizes.")
        print("   4 - Multiplicação de uma matriz por um escalar.")
        print("   5 - Sair do progama")
        
        # loop com ordem de parada para que o progama aceite a entrada correta
        while True:
            
            opcao = int(input("Insira uma opção abaixo: "))
            
            if opcao >= 1 and opcao <= 5:
                break
            # parar a execução do loop caso o usuário queira terminar o progama
            elif(opcao == 5): 
                break
            else:
                print("Entrada errada. Digite novamente.\n")
        
        # parada geral do progama
        if(opcao == 5):
            break
        
        # indo para próximas linhas
        print("\n")
        
        # recendo a quantidade de linhas e colunas das matrizes
        linhaA = int(input("Informe a quantidade de linhas da matriz A: "))
        colunaA = int(input("Informe a quantidade de colunas da matriz A: "))
        linhaB = int(input("Informe a quantidade de linhas da matriz B: "))
        colunaB = int(input("Informe a quantidade de colunas da matriz B: "))
        
        # inicializando as matrizes com suas devidas ordens e com lixo de memória
        A = np.empty([linhaA, colunaA], dtype = float) 
        B = np.empty([linhaB, colunaB], dtype = float)
        
        # indo para próxima linha
        print("\n")
        
        # estrutura de repetição for para implementar os elementos da matriz A
        for i in range(0, linhaA):
            for j in range(0, colunaA):
                A[i][j] = float(input("Digite o elemento [{}][{}] da matriz A: ".format(i + 1,j + 1)))
        
        # indo para próxima linha
        print("\n")
        
        # estrutura de repetição for para implementar os elementos da matriz B
        for i in range(0, linhaB):
            for j in range(0, colunaB):
                B[i][j] = float(input("Digite o elemento [{}][{}] da matriz B: ".format(i + 1, j + 1)))
        
        # indo para próxima linha
        print("\n")
        
        # imprime a matriz A
        print("A matriz A é: \n{}".format(A))
        
        # indo para próxima linha
        print("\n")
        
        # imprime a matriz B
        print("A matriz B é: \n{}".format(B))
        
        # recebe um escalar para ser usado na função da opção 4
        if(opcao == 4):
            escalar = float(input("\nInforme um escalar: "))
        
        # indo para próxima linha
        print("\n")
        
        # caso o usário escolha a opção 1, relativa a soma
        if(opcao == 1):
            print("\nSoma:\n\n {}".format(soma(A, linhaA, colunaA, B, linhaB, colunaB)))
        # se não se, o usuário escolher a opção 2, realtivo a subtração
        elif(opcao == 2):
            print("\nSubtração: \n\n{}".format(subtracao(A, linhaA, colunaA, B, linhaB, colunaB)))
        # se não se, o usuário escolher a opção 3, realtivo a multiplicação
        elif(opcao == 3):
            print("\nMultiplicação: \n\n{}".format(multiplicacao(A, linhaA, colunaA, B, linhaB, colunaB)))
        # se não se, o usuário escolher a opção 4, realtivo a multiplicação de um escalar com uma matriz
        elif(opcao == 4):
            print("\nMultiplicação de um escalar com uma matriz: \n\n{}".format(multiplicaEscalar(A, B, escalar)))
    
    return 0


# função que realiza a soma entre duas matrizes
def soma(matrizA, linhaA, colunaA, matrizB, linhaB, colunaB):
    
    # verificando se a operação está definida
    if(linhaA != linhaB or colunaA != colunaB):
        # retornando a mensagem de erro caso não seja uma operação compatível
        return "operação com tais matrizes incompatíveis. Tente novamente."
        
    # definindo a soma
    somando = matrizA + matrizB
    
    # retornando o resultado da função
    return somando



# função que realiza a subtração de duas matrizes
def subtracao(matrizA, linhaA, colunaA, matrizB, linhaB, colunaB):
    
    # verificando se a operação está definida
    if(linhaA != linhaB or colunaA != colunaB):
        # retornando uma mensagem de erro caso a operação não seja compatível
        return "operação com tais matrizes incompatíveis. Tente novamente."
    
    #escolhendo a subtração
    print("1) A - B = ??")
    print("2) B - A = ??")
    
    # recebendo a opção informada acima e verificando se foi digitado corretamente
    while True:
        opcao = int(input("Informe sua opção: "))
        if(opcao == 1 or opcao == 2):
            break
        else:
            print("Opção inválida, digite novamente.\n")
    
    #realizando a operação
    if(opcao == 1):
        # definindo a operação de subtração
        subtraindo = matrizA - matrizB
        # retornando o resultado da função
        return subtraindo
    elif(opcao == 2):
        # definindo a operação de subtração
        subtraindo = matrizB - matrizA
        # retornando o resultado da função
        return subtraindo
    
    
# função que realiza  a multiplicação de duas matrizes
def multiplicacao(matrizA, linhaA, colunaA, matrizB, linhaB, colunaB):
    
    #escolhendo a multiplicação
    print("1) A x B = ??")
    print("2) B x A = ??")
    
    # recebendo a opção informada acima e fazendo uma verificação de segurança
    while True:
        opcao = int(input("Informe sua opção: "))
        if(opcao == 1 or opcao == 2):
            break
        else:
            print("Opção inválida, digite novamente.\n")
    
    # verificando se a operação está definida
    if(opcao == 1):
        if(colunaA != linhaB):
            # retorna uma mensagem de erro caso a operação não seja compatível
            return "operação com tais matrizes incompatíveis. Tente novamente."
    elif(opcao == 2):
        if(colunaB != linhaA):
            # retorna uma mensagem de erro caso a operação não seja compatível
            return "operação com tais matrizes incompatíveis. Tente novamente."
    
    #realizando a operação
    if(opcao == 1):
        # definindo a operação de multiplicação
        multiplicando = np.dot(matrizA, matrizB)
        # retornando o resultado da função
        return multiplicando
    elif(opcao == 2):
        # definindo a operação de multiplicação
        multiplicando = np.dot(matrizB,matrizA)
        # retornando o resultado da função
        return multiplicando
    

# função que  multiplica um escalar pela matriz
def multiplicaEscalar(matrizA, matrizB, escalar):
    
    # escolhendo a matriz
    print("Qual matriz você quer multiplicar pelo escalar?")
    print("1) matriz A")
    print("2) matriz B")
    
    # recebendo a opção informada acima e fazendo uma verificação de segurança
    while True:
        opcao = int(input("Informe sua opção: "))
        if(opcao == 1 or opcao == 2):
            break
        else:
            print("Opção inválida, digite novamente.\n")
          
    if(opcao == 1):
        # definindo a multiplicação da matrizA por um escalar
        novaMatriz = escalar * matrizA
        # retornando o resultado da função
        return novaMatriz
    elif(opcao == 2):
        # definindo a multiplicação da matrizB por um escalar
        novaMatriz = escalar * matrizB
        # retornando o resultado da função
        return novaMatriz


if __name__ == '__main__':
    main() # chamada da função main