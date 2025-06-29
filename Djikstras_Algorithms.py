
class WeightedDirectedGraph:

    def __init__(self):
        self.adjlist = {}  # Dictionary of vertex: [(neighbor, weight)]

    def addVertex(self, vertex):
        if vertex not in self.adjlist:
            self.adjlist[vertex] = []
        else:
            print(f"The vertex {vertex} already exists")

    def addEdge(self, from_vertex, to_vertex, weight):
        if from_vertex not in self.adjlist:
            print(f"{from_vertex} does not exist")
            return
        if to_vertex not in self.adjlist:
            print(f"{to_vertex} does not exist")
            return
        self.adjlist[from_vertex].append((to_vertex, weight))

    def removeEdge(self, from_vertex, to_vertex):
        new_neighbours = []
        for neighbour_vertex, weight in self.adjlist[from_vertex]:
            if neighbour_vertex != to_vertex:
                new_neighbours.append((neighbour_vertex, weight))  # FIXED
        self.adjlist[from_vertex] = new_neighbours

    def printGraph(self):
        for vertex in self.adjlist:
            print(f"{vertex} --> {self.adjlist[vertex]}")

    def DjikstasAlgorithims(self, start_vertex):
        import heapq
        distances = {vertex: float('inf') for vertex in self.adjlist}
        distances[start_vertex] = 0

        visited_vertices = set()
        priorityqueue = []
        heapq.heappush(priorityqueue, (0, start_vertex))

        while priorityqueue:
            current_cost, current_vertex = heapq.heappop(priorityqueue)

            if current_vertex in visited_vertices:
                continue
            visited_vertices.add(current_vertex)

            for neighbour_vertex, edge_weight in self.adjlist[current_vertex]:
                new_distance = current_cost + edge_weight
                if new_distance < distances[neighbour_vertex]:
                    distances[neighbour_vertex] = new_distance
                    heapq.heappush(priorityqueue, (new_distance, neighbour_vertex))

        return distances  # FIXED: moved outside while loop


# ---- USAGE ----
graph = WeightedDirectedGraph()
graph.addVertex("A")
graph.addVertex("B")
graph.addVertex("C")
graph.addVertex("D")
graph.addVertex("E")
graph.addVertex("F")

graph.addEdge("A", "B", 5)
graph.addEdge("A", "C", 2)
graph.addEdge("B", "D", 1)
graph.addEdge("D", "E", 11)
graph.addEdge("D", "F", 4)

graph.printGraph()

# Run Dijkstra's algorithm from vertex A
distances_from_A = graph.DjikstasAlgorithims("A")

# Output the shortest paths
print("\nShortest distances from A:")
for vertex, distance in distances_from_A.items():
    print(f"A to {vertex}: {distance}")
