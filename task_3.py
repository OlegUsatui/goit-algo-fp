import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))

    def dijkstra(self, src):
        min_heap = [(0, src)]  # (distance, vertex)
        distances = [float('inf')] * self.V
        distances[src] = 0

        while min_heap:
            dist, u = heapq.heappop(min_heap)

            # Visit each neighbor of u
            for neighbor, weight in self.graph[u]:
                if distances[u] + weight < distances[neighbor]:
                    distances[neighbor] = distances[u] + weight
                    heapq.heappush(min_heap, (distances[neighbor], neighbor))

        return distances

# Test
g = Graph(9)
g.add_edge(0, 1, 4)
g.add_edge(0, 7, 8)
g.add_edge(1, 2, 8)
g.add_edge(1, 7, 11)
g.add_edge(2, 3, 7)
g.add_edge(2, 8, 2)
g.add_edge(2, 5, 4)
g.add_edge(3, 4, 9)
g.add_edge(3, 5, 14)
g.add_edge(4, 5, 10)
g.add_edge(5, 6, 2)
g.add_edge(6, 7, 1)
g.add_edge(6, 8, 6)
g.add_edge(7, 8, 7)
print(g.dijkstra(0))
