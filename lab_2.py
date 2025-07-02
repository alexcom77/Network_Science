import networkx as nx
G = nx.Graph()

# добавление в граф 27 узлов:
G.add_nodes_from(range(27))

# добавление рёбер (этап «яма»):
for i in range(4):
    G.add_edge(i, i+1)  # 0-1, 1-2, ..., 3-4
G.remove_edge(3, 4)
G.add_edge(4, 5)

# добавление рёбер (этап «подъём»):
for i in range(5, 8):
    G.add_edge(i, i+1)  # 5-6, 6-7, 7-8
G.add_edge(8, 6)
G.add_edge(8, 7)
G.add_edge(8, 9)

#добавление рёбер (этап «падение»):
for i in range(9, 26):
    G.add_edge(i, i+1)  # 9-10, ..., 26-27

# вычисление центральности узлов:
centrality = nx.eigenvector_centrality(G, max_iter=1000)

# сортировка и вывод значений центральности:
sorted_values = [centrality[i] for i in range(27)]
print("Централизация узлов:", sorted_values)