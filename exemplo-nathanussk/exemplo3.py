import numpy as np
import matplotlib.pyplot as plt

# Gerando valores para o eixo x do plano cartesiano
x = np.arange(0, 2.0*np.pi, 0.01)
# Passando os valores gerados para a variável x na função seno e salvando em y
y = np.sin(x)
# plotando o gráfico usando os valores de x e y
# Crie uma figura de 8 x 6 polegadas, 80 pontos por polegada
plt.figure(figsize=(8, 6), dpi=80)
# Pssando os eixos X e Y como parâmetros, nomeado o gráfico
# colocando a cor do gráfico para purple
plt.plot(x, y, color="purple", label="Seno", linewidth=5.0)
# Adicionando um Título para o gráfico
plt.title("Gráfico da função seno", fontsize=17)
# Nomeado os eixos X e Y
plt.xlabel("Eixo X", fontsize=15)
plt.ylabel("Eixo Y", fontsize=15)
# Colocando uma legenda no canto superior esquerdo da imagem gerada
plt.legend(loc="upper left")
# Esse método é quem gera a plotagem do gráfico
plt.show()