import sys 
 
class Graph(): 
 
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)] 
 
    def printSolution(self, dist): 
        print("Vertex \tDistance from Source") 
        for node in range(self.V): 
            print(node, "\t", dist[node]) 
 
    def minDistance(self, dist, sptSet): 
 
        min = sys.maxsize 
 
        for u in range(self.V): 
            if dist[u] < min and sptSet[u] == False: 
                min = dist[u] 
                min_index = u 
 
        return min_index 
 
    def dijkstra(self, src): 
 
        dist = [sys.maxsize] * self.V 
        dist[src] = 0 
        sptSet = [False] * self.V 
 
        for cout in range(self.V): 
 
            x = self.minDistance(dist, sptSet) 
            sptSet[x] = True 
 
            for y in range(self.V): 
                if self.graph[x][y] > 0 and sptSet[y] == False and dist[y] > dist[x] + self.graph[x][y]: 
                    dist[y] = dist[x] + self.graph[x][y] 
 
        self.printSolution(dist) 
 
if __name__ == "__main__": 
    g = Graph(5) 
    g.graph = [[0, 2, 0, 6, 0], 
            [2, 0, 3, 8, 5], 
            [0, 3, 0, 0, 7], 
            [6, 8, 0, 0, 9], 
            [0, 5, 7, 9, 0]] 
 
    g.dijkstra(0)