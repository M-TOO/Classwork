
class WeightedDirectedGraph:

    def __init__(self):
        self.adjlist = {}  # Dictionary of vertex: [(neighbor, weight)]

#Vertex is a node
    def add_vertex(self, vertex):
        #Adding a node to the list
        if vertex not in self.adjlist:
            self.adjlist[vertex] = []
        else:
            print(f"The vertex {vertex} already exists")

    def add_edge(self, from_vertex, to_vertex, weight):
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

    def print_graph(self):

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

        return distances


if __name__=="__main__":

    graph = WeightedDirectedGraph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")
    graph.add_vertex("E")
    graph.add_vertex("F")

    graph.add_edge("A", "B", 5)
    graph.add_edge("A", "C", 2)
    graph.add_edge("B", "D", 1)
    graph.add_edge("D", "E", 11)
    graph.add_edge("D", "F", 4)

    graph.print_graph()


    distances_A = graph.DjikstasAlgorithims("A")

    # Output the shortest paths
    print("\nThe shortest distances from A:")
    for vertex, distance in distances_A.items():
        print(f"A to {vertex}: {distance}")
