class DFSGraph:
    def __init__(self, size):
        self.adj_matrix = [[0]*size for _ in range(size)]
        self.size = size
        self.vertex_data = ['']*size

    def print_graph(self):
        print('Adjacency matrix: ')
        for row in self.adj_matrix:
            print(' '.join(map(str,row)))

        print('Vertex data: ')
        for vertex,data in enumerate(self.vertex_data):
            print(f"Vertex {vertex}: {data}")

    def add_vertex_data(self, vertex, data):
        if 0<=vertex<self.size:
            self.vertex_data[vertex] = data 
        else:
            print('Vertex not in range')

    def add_edge(self, vertex1, vertex2):
        if 0<=vertex1<self.size and 0<=vertex2<self.size:
            self.adj_matrix[vertex1][vertex2] = 1 
            self.adj_matrix[vertex2][vertex1] = 1

    def dfs_utils(self, visited, start_vertex):
        visited[start_vertex] = True
        print(self.vertex_data[start_vertex], end=' ')
        for i in range(self.size):
            if self.adj_matrix[start_vertex][i] == 1 and visited[i] == False:
                self.dfs_utils(visited, i)
            
    def dfs(self, start_vertex_data):
        visited = [False]*self.size
        start_vertex = self.vertex_data.index(start_vertex_data)
        self.dfs_utils(visited, start_vertex)


g = DFSGraph(7)

g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_vertex_data(4, 'E')
g.add_vertex_data(5, 'F')
g.add_vertex_data(6, 'G')

g.add_edge(3, 0)  # D - A
g.add_edge(0, 2)  # A - C
g.add_edge(0, 3)  # A - D
g.add_edge(0, 4)  # A - E
g.add_edge(4, 2)  # E - C
g.add_edge(2, 5)  # C - F
g.add_edge(2, 1)  # C - B
g.add_edge(2, 6)  # C - G
g.add_edge(1, 5)  # B - F

g.print_graph()  
print("\nDepth First Search starting from vertex D:")
g.dfs('D')