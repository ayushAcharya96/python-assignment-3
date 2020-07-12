import sys
# Dijkstra's  Algorithm


class Graph:
    def __init__(self, edges):
        # self.vertices = vertices
        self.edges = edges
        self.selected_nodes = []
    
    def min_dist(self, node, result_dist):
        min_dist = sys.maxsize
        min_index = 0
        for v in range((len(self.edges))):
            # print(result_dist[v])
            print(result_dist[v] > 0 and v not in self.selected_nodes)
            print(self.selected_nodes)
            if self.edges[node][v] != 0  and v not in self.selected_nodes:
                min_dist = result_dist[v]
                min_index = v
        return min_index
    

    def dijkstra_algorithm(self, start):
        node = start
        result_dist = { key : sys.maxsize for key in range(len(self.edges))}
        result_dist[start] = 0
        self.selected_nodes.append(node)
        print(result_dist)
        for i in range(len(self.edges)):
            if True:
                node = self.min_dist(i, result_dist)
                # print(node)
                self.selected_nodes.append(node)
                for j in range(len(self.edges)):
                    if self.edges[i][j] != 0 and j in self.selected_nodes:
                        result_dist[j] = result_dist[i] + self.edges[i][j]
        print('Vertices \t Minimum Distance from Source')
        for node in self.selected_nodes:
            print(f'{node} \t {result_dist[node]}')




graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
        [4, 0, 8, 0, 0, 0, 0, 11, 0], 
        [0, 8, 0, 7, 0, 4, 0, 0, 2], 
        [0, 0, 7, 0, 9, 14, 0, 0, 0], 
        [0, 0, 0, 9, 0, 10, 0, 0, 0], 
        [0, 0, 4, 14, 10, 0, 2, 0, 0], 
        [0, 0, 0, 0, 0, 2, 0, 1, 6], 
        [8, 11, 0, 0, 0, 0, 1, 0, 7], 
        [0, 0, 2, 0, 0, 0, 6, 7, 0] 
        ];

dij = Graph(graph)
dij.dijkstra_algorithm(0)