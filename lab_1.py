import heapq
def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances
graph = {
    'A': {'B': 3, 'C': 8},
    'B': {'A': 3, 'D': 4, 'E': 9},
    'C': {'A': 8, 'D': 2, 'E': 5},
    'D': {'B': 3, 'C': 3, 'E': 2,'F': 4},
    'E': {'C': 6, 'D': 2, 'F': 11},
    'F': {'B': 9, 'D': 4, 'E': 11}
}
result = dijkstra(graph, 'A')
print("Кратчайшие расстояния до каждой вершины:")
for vertex, distance in result.items():
    print(f"До вершины {vertex}: {distance}")
