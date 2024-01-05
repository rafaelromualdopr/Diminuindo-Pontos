#QUESTAO 1 CORRIGIDA

# Define os pontos do polígono inicial
points = [(1, 1), (1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (3, 3), (3,2), (2,2), (2,1), (1,1)]

# Define uma função que recebe uma lista de pontos e retorna uma lista reduzida
def reduzir_pontos(points):
  # Cria uma lista vazia para armazenar os pontos reduzidos
  pontos_reduzidos = []

  # Adiciona o primeiro ponto à lista de pontos reduzidos
  pontos_reduzidos.append(points[0])

  # Percorre todos os pontos da lista original, exceto o primeiro e o último
  for i in range(1, len(points)-1):
    # Obtém o ponto atual, o anterior e o próximo
    ponto_atual = points[i]
    ponto_anterior = points[i - 1]
    ponto_proximo = points[i + 1]
    # Calcula o produto vetorial entre os vetores formados pelos pontos
    produto_vetorial = (ponto_atual[0] - ponto_anterior[0]) * (ponto_proximo[1] - ponto_atual[1]) - (ponto_atual[1] - ponto_anterior[1]) * (ponto_proximo[0] - ponto_atual[0])
    # Se o produto vetorial for diferente de zero, significa que o ponto atual não é colinear com os seus vizinhos
    if produto_vetorial != 0:
      # Adiciona o ponto atual à lista de pontos reduzidos
      pontos_reduzidos.append(ponto_atual)

  # Adiciona o último ponto à lista de pontos reduzidos
  pontos_reduzidos.append(points[-1])

  # Retorna a lista de pontos reduzidos
  return pontos_reduzidos

print("Pontos iniciais: {}".format(points))
pontos_reduzidos = reduzir_pontos(points)
print(pontos_reduzidos)

# Importa a biblioteca matplotlib
import matplotlib.pyplot as plt
# Separa as coordenadas x e y dos pontos
x = [p[0] for p in pontos_reduzidos]
y = [p[1] for p in pontos_reduzidos]
# Cria um gráfico de linhas com os pontos
plt.plot(x, y, 'b-')
# Adiciona os pontos como marcadores
plt.plot(x, y, 'ro')
# Define os limites do eixo x e y
plt.xlim(0, 4)
plt.ylim(0, 5)
# Mostra o gráfico na tela
plt.show()