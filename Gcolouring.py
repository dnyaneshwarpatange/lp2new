class GraphColoring: 
    def __init__(self, graph, colors): 
        self.graph = graph 
        self.colors = colors 
        self.num_vertices = len(graph) 
        self.solution = [-1] * self.num_vertices 
 
    def is_safe(self, vertex, color): 
        for neighbor in range(self.num_vertices): 
            if self.graph[vertex][neighbor] == 1 and self.solution[neighbor] == color: 
                return False 
        return True 
 
    def solve_graph_coloring(self, vertex): 
        if vertex == self.num_vertices: 
            return True 
 
        for color in self.colors: 
            if self.is_safe(vertex, color): 
                self.solution[vertex] = color 
 
                if self.solve_graph_coloring(vertex + 1): 
                    return True 
 
                self.solution[vertex] = -1 
 
        return False 
 
    def solve(self): 
        if self.solve_graph_coloring(0): 
            print("Solution exists:") 
            for vertex, color in enumerate(self.solution): 
                print("Vertex", vertex, "-> Color", color) 
        else: 
            print("No solution exists.") 
 
# Example usage 
graph = [[1, 0, 1, 0], 
         [1, 0, 1, 0], 
         [1, 1, 0, 1], 
        [0, 1, 1, 1]] 
 
colors = [1, 2, 3]  # Available colors 
 
graph_coloring = GraphColoring(graph, colors) 
graph_coloring.solve() 