# importando a biblioteca numpy do Python
import numpy as np

# importando a biblioteca de funções do Python matplotlib
import matplotlib.pyplot as plt


# definindo a matriz A a partir da tabela 1
A = np.array([[213, 651, 304, 420],
              [225, 688, 321, 441],
              [237, 726, 338, 468],
              [249, 764, 356, 492]])

# imprimindo a matriz A
print("A matriz A é\n\n", A)

# definindo a matriz B a partir da tabela 2
B = np.array([[1.0, 0.0, 1.0, 0.0],
              [0.0, 0.0, 0.0, 2.0],
              [0.4, 0.5, 0.0, 0.0],
              [0.0, 0.0, 0.5, 2.0],
              [0.4, 0.5, 0.0, 0.0]])

# imprimindo a matriz B
print("A matriz B é\n\n", B)

# x recebe a quarta linha de A
x = A[3]

# x é transposta para se tornar um vetor-coluna
x = np.transpose(x)

# realizando a multiplicação da matriz B com a matriz x
Calorias = np.dot(B, x)

# imprimindo a matriz de calorias gastas por semana
print("A matriz com valores de calorias gastas é:\n\n", Calorias)

# esquematizando as etiquetas do gráfico no eixo x
DiasdaSemana = ['Segunda-feira', 'Terça-feira',
                'Quarta-feira', 'Quinta-feira', 'Sexta-feira']

# definindo as dimensões do gráfico
plt.figure(figsize=(8, 5))
# definindo a legenda do eixo x
plt.xlabel('Dias da Semana')
# definindo as legendas do eixo y
plt.ylabel('Calorias Gastas')
# plotando o gráfico e definindo uma legenda
plt.plot(DiasdaSemana, Calorias, label='Calorias Gastas/Dia')
# chamando a legenda para ser exposta no gráfico
plt.legend()
# definindo um input diferente de 0 para entrada verdadeira na grade do gráfico
plt.grid(True)
# definindo o título do gráfico
plt.title('Gráfico de Calorias Gastas por Alysson')

# definindo as dimensões do gráfico
plt.figure(figsize=(8, 5))
# definindo a legenda do eixo x
plt.xlabel('Dias da Semana')
# definindo as legendas do eixo y
plt.ylabel('Calorias Gastas')
# plotando o gráfico e definindo uma legenda
plt.barh(DiasdaSemana, Calorias, label='Calorias Gastas/Dia')
# chamando a legenda para ser exposta no gráfico
plt.legend()
# definindo um input diferente de 0 para entrada verdadeira na grade do gráfico
plt.grid(True)
# definindo o título do gráfico
plt.title('Gráfico de Calorias Gastas por Alysson')

# definindo a matriz C baseada na tabela 3
C = np.array([[0.10, 0.30, 0.15],
              [0.30, 0.40, 0.25],
              [0.10, 0.20, 0.15]])

# imprimindo a matriz C
print("A matriz C é:\n\n", C)

# definindo a matriz D baseado na tabela 4
D = np.array([[4000, 4500, 4500, 4000],
              [2000, 2600, 2400, 2200],
              [5800, 6200, 6000, 6000]])

print("A matriz D é:\n\n", D)

# realizando a multiplicação da matriz C com a matriz D
Custos = np.dot(C, D)

# imprime a matriz de custos por trimeste em cada categoria, em reais
print("A matriz de Custos é:\n\n", Custos)

# esquematizando as etiquetas do gráfico no eixo x
Trimestres = ['Verão', 'Outono', 'Inverno', 'Primaveira']
# definindo os valores gastos apenas na categoria Matéria-Prima
MateriaPrima = Custos[0]
# definindo os valores gastos apenas na categoria Pessoal
Pessoal = Custos[1]
# definindo os valores gastos apenas na categoria Despesas Gerais
DespesasGerais = Custos[2]

# definindo as dimensões do gráfico
plt.figure(figsize=(12, 8))
# definindo a legenda do eixo x
plt.xlabel('Trimestres')
# definindo a legenda do eixo y
plt.ylabel('Dinheiro(R$)')
# plotando o gráfico para a categoria Matéria-Prima, com sua respectiva legenda
plt.plot(Trimestres, MateriaPrima, label='Matéria-Prima')
# plotando o gráfico para a categoria Pessoal, com sua respectiva legenda
plt.plot(Trimestres, Pessoal, label='Pessoal')
# plotando o gráfico para a categoria Despesas Gerais, com sua respectiva legenda
plt.plot(Trimestres, DespesasGerais, label='Despesas Gerais')
# chamando a legenda para ser exposta no gráfico
plt.legend()
# definindo um input diferente de 0 para entrada verdadeira na grade do gráfico
plt.grid(True)
# definindo o título do gráfico
plt.title('Gráfico de Custos por Categoria em cada Trimestre')
