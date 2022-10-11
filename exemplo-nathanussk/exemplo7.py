# importando a biblioteca de funções numpy do Python
import numpy as numpy

# Função responsável por retornar o equivalente numérico para as letras do alfabeto


def equivalenteDecimal(letra):

    # definindo uma cadeia de caracteres com todas as letras do alfabeto
    alfabeto = "zabcdefghijklmnopqrstuvwxy"

    # encontra a posição da letra na string e a retorna
    return (alfabeto.find(letra))

# função responsável por retornar o equivalente alfabético para um valor numérico


def equivalenteAlfabetico(numero):

    # definindo uma cadeia de caracteres com todas as letras do alfabeto
    alfabeto = "zabcdefghijklmnopqrstuvwxy"

    # encontra o pedaço da string a qual o número correspondente indica
    return (alfabeto[numero])


# criando uma matriz A, responsável pela segurança da criptografia
# definindo a matriz A
A = numpy.array([[5, 6], [2, 3]])

# função responsável por codificar nossa matriz, dependendo da matriz inserida
# veremos mais abaixo que uma entrada específica de outra matriz é suficiente para decodificar nossa matriz


def cifraHill(texto, chave):

    # inicializa a variável que vai receber a mensagem codificada
    codigo = ""
    # criando uma matriz responsável por receber o valor númerico equivalente ao alfabético
    valorNumerico = numpy.empty([2, 1], dtype=int)
    # as inicializações indicam que ela será um vetor-coluna do tipo inteiro

    # criando uma matriz responsável por receber o valor codificado equivalente ao alfabético
    valorCodificado = numpy.empty([2, 1], dtype=int)
    # as inicializações indicam que ela será um vetor-coluna do tipo inteiro

    # estrutura de repetição for responsável para codificar cada par do texto formado
    for indice in range(0, len(texto)):

        # estrutura de seleção if responsável por adicionar o valor numérico para a primeira letra do par
        if (indice == 0 or indice % 2 == 0):

            # pega exatamente a letra localizada no elemento numerico de 'indice'
            valor = equivalenteDecimal(texto[indice])
            # adiciona na primeira linha da primeira coluna
            valorNumerico[0][0] = valor

        # estrutura de seleção responsável por adicionar o valor numérico para a segunda letra do par
        if (indice != 0 and indice % 2 != 0):

            # pega exatamente a letra localizada no elemento numerico de 'indice'
            valor = equivalenteDecimal(texto[indice])
            # adiciona na segunda linha da primeira coluna
            valorNumerico[1][0] = valor

        # estrutura de seleção responsável por calcular a multiplicação da matriz A pelo vetor-coluna
        # dos pares numéricos
        if (indice != 0 and indice % 2 != 0):
            # realiza a multiplicação da matriz A com os pares de números equivalentes a letras
            valorCodificado = numpy.dot(chave, valorNumerico)

            # caso o valor do resultado codificado no primeiro par da letra seja maior que 25,
            # substitui pelo valor
            # do seu módulo por 26
            if (valorCodificado[0][0] > 25):
                valorCodificado[0][0] = (valorCodificado[0][0] % 26)

            # caso o valor do resultado codificado no segundo par da letra seja maior que 25,
            # substitui pelo valor
            # do seu módulo por 26
            if (valorCodificado[1][0] > 25):
                valorCodificado[1][0] = (valorCodificado[1][0] % 26)

            # pega o equivalente alfabético para os novos números codificados, visando
            # construir a frase codificada
            # primeira linha do vetor-coluna
            a = str(equivalenteAlfabetico(valorCodificado[0][0]))
            # segunda linha do vetor-coluna
            b = str(equivalenteAlfabetico(valorCodificado[1][0]))

            # adiciona letra por letra codificada a uma variável string para montar a frase
            codigo += a
            codigo += b

    # remove os caracteres desnecessários e mostra somente a parte codificada
    codigo = codigo[len(codigo) - len(texto): len(codigo)]

    # função retorna código
    return codigo


# função responsável por pegar o texto a ser encriptado
def inserirFrase():

    texto = ""  # inicializando uma variável vazia
    # padrão de entrada para receber uma string
    texto = str(input("Informe um texto sem acentos: "))
    texto = texto.replace(" ", "")  # eliminando os espaços em branco do texto
    texto = texto.lower()  # deixando toda a string com letras minúsculas

    # caso o texto tenha uma quantidade ímpar de letras, adiciona mais uma letra arbitrária ao final
    if (len(texto) % 2 != 0):
        texto += "g"  # adiciona-se g, por exemplo

    print("o texto é: {}".format(texto))  # imprime o texto informado na tela

    return texto  # retorna a frase pronta para o sistema de criptografia


# chama a função para adicionar um texto a variável
texto = inserirFrase()
# a opção por criar tal função advém da necessidade da frase ter que atender aos requisitos
# informados acima para ser codificada

cifraHill(texto, A)  # função responsável por criptografar o texto
# entrada do parâmetro da string de texto e da matriz chave

# imprime a matriz A
print("{}".format(A))

# definindo a matriz A
A = numpy.array([[5, 6], [2, 3]])
# calculando o resíduo (ad - bc)
residuo = (A[0][0] * A[1][1] - A[0][1] * A[1][0]) % 26
# temos a.a^{-1} = 1 (mod 26)
# residuo.reciproco = x  = 1 (mod 26)

# imprime o residuo
print("{}".format(residuo))

# definindo o reciproco
reciproco = 9
# definindo o posicionamento da matriz invertível (mod 26)
descriptografia = numpy.array([[A[1][1], -A[0][1]], [-A[1][0], A[0][0]]])
# realizando a multiplicação com o recíproco
descriptografia *= reciproco
# definindo o módulo 26 de cada elemento
descriptografia %= 26

# imprimindo a matriz descriptograda
print("{}".format(descriptografia))

# definindo a cifra criptografada, dada anteriormente pela criptografia com A
cifra = "fhgviocepytuidezsmxeikizijywylmcnfylyhembe"

# chamando a função responsável por criptografar/descriptografar
cifraHill(cifra, descriptografia)

# chama a função para receber uma frase e configurá-la para a criptografia
frase = inserirFrase()
# A Frase é: "Quem Estuda Passa"

cifraHill(frase, A)  # imprime a frase criptografada

# vamos inserir a frase criptografada
frase = inserirFrase()

# vamos encriptar uma segunda camada
cifraHill(frase, A)

# vamos inserir a frase encriptada por duas vezes consecutivas
frase = inserirFrase()

# vamos descriptografar a primeira camada
cifraHill(frase, descriptografia)

# vamos inserir a frase novamente para quebrar a segunda e última camada
frase = inserirFrase()

# por fim, vamos descriptografar por completo
cifraHill(frase, descriptografia)
