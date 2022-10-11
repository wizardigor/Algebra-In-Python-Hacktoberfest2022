# Importa Funções da biblioteca Numpy
import numpy as np

# função que calcula o determinante de uma matriz


def determinante():

    # Recebe a ordem da matriz
    qtd = int(input('Informe o ordem da matriz: '))

    # Inicializa a matriz, ainda com 'lixo de endereços de memória' nele
    matriz = np.empty([qtd, qtd], dtype=float)
    print('\n')

    # Adiciona elementos na matriz
    for i in range(0, qtd):
        for j in range(0, qtd):
            matriz[i][j] = float(
                input('Digite [{}][{}] da matriz: '.format(i + 1, j + 1)))

    # Imprime a matriz
    print('\nA matriz é:\n', matriz)

    # a variável 'determinante' recebe o determinante da matriz
    determinante = np.linalg.det(matriz)

    # Imprime o determinante
    print('\nO determinante da matriz é: {:.2f}.'.format(determinante))

    # função não retorna nada
    return None


# imprimindo a função determinante
determinante()
