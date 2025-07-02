import networkx as nx
# Задаем параметры для создания графа
n = 19
p = 0.95
# Создаём граф G с помощью модели Эрдёша — Реньи
G = nx.erdos_renyi_graph(n, p)
# Рассчитываем среднюю степень вершин графа
a = 0
for n in G.nodes():
    a = a + G.degree(n)
a_avr = float(a) / len(G.nodes())
calc_avr = (n-1)*p
div_a = calc_avr - a_avr
print("Средняя степень вершины фактическая: ", round(a_avr, 3))
print("Средняя степень вершины по формуле: ", round(calc_avr, 3))
print("Полученная разница значений: ", round(div_a, 3))